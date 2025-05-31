import os
import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
from emoji_config import get_emoji, get_all_emojis_for_letter
import json
import signal
import sys
import asyncio

# Load environment variables
load_dotenv()

# Load letter patterns from JSON
with open('letter_patterns.json', 'r') as f:
    LETTER_PATTERNS = json.load(f)

# Bot setup
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

@bot.event
async def on_disconnect():
    print("Bot is disconnecting...")

@bot.event
async def on_shutdown():
    print("Bot is shutting down...")
    await bot.close()

def signal_handler(sig, frame):
    print("\nShutting down bot...")
    # Get the current event loop
    loop = asyncio.get_event_loop()
    # Create a task to close the bot
    loop.create_task(bot.close())
    # Stop the event loop
    loop.stop()
    sys.exit(0)

@bot.tree.command(name="message", description="Convert your message to powerline!")
async def message(interaction: discord.Interaction, text: str):
    """
    Convert text to emoji art representation
    Args:
        text: The text to convert
    """
    # Keep spaces but remove other punctuation
    filtered_text = ''.join(c if c.isspace() else c.lower() for c in text if c.isalnum() or c.isspace())
    
    if not filtered_text:
        await interaction.response.send_message("Please enter some text with letters or numbers!")
        return
    
    # Process all characters in groups of 5
    for i in range(0, len(filtered_text), 5):
        chars = filtered_text[i:i+5]  # Get next 5 characters
        
        # Process each line (1-6) for all characters
        message_rows = []
        for line_num in range(1, 7):  # For each line (1-6)
            row_emojis = []
            for char in chars:  # For each character
                # Get the line pattern for this character
                line_key = f"line_{line_num}"
                if line_key in LETTER_PATTERNS["LETTER_PATTERNS"][char]:
                    line_pattern = LETTER_PATTERNS["LETTER_PATTERNS"][char][line_key]
                    # Convert each emoji name to Discord format
                    row_emojis.extend([get_emoji(emoji.strip()) for emoji in line_pattern])
            # Join all emojis in this row with no spaces
            message_rows.append(''.join(row_emojis))
        
        # Join all rows with newlines
        final_message = '\n'.join(message_rows)
        
        # Send the emoji message
        if i == 0:
            # First message uses interaction.response
            await interaction.response.send_message(final_message)
        else:
            # Subsequent messages use interaction.channel.send
            await interaction.channel.send(final_message)

@bot.tree.command(name="show_emojis", description="Show all available emojis for a letter")
async def show_emojis(interaction: discord.Interaction, letter: str):
    """
    Show all available emojis for a given letter
    Args:
        letter: The letter to show emojis for
    """
    if len(letter) != 1:
        await interaction.response.send_message("Please enter a single letter!")
        return
    
    emojis = get_all_emojis_for_letter(letter)
    response = f"Emojis for '{letter}':\n" + " ".join(emojis)
    await interaction.response.send_message(response)

# Set up signal handler for graceful shutdown
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

# Run the bot
bot.run(os.getenv('DISCORD_TOKEN'))