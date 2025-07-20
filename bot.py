# TODO: Add make bot send message in logs when user uses swearword

import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from emoji_config import get_emoji
from regex import contains_swearword
import json
import random

# Load environment variables
load_dotenv()

# Load letter_patterns from JSON
with open('letter_patterns.json', 'r') as f:
    LETTER_PATTERNS = json.load(f)

def convert_characters_to_emoji(characters):
    """
    Convert a group of characters to emoji art
    Args:
        characters (str): Up to 3 characters to convert
    Returns:
        str: Multi-line emoji art
    """
    message_rows = []
    
    # Create 6 lines of emoji art
    for line_num in range(1, 7):
        row_emojis = []
        
        # Process each character in the group
        for char in characters:
            line_key = f"line_{line_num}"
            char_patterns = LETTER_PATTERNS["LETTER_PATTERNS"].get(char, {})
            
            if line_key in char_patterns:
                # Convert emoji names to Discord format
                emoji_pattern = char_patterns[line_key]
                row_emojis.extend([get_emoji(emoji.strip()) for emoji in emoji_pattern])
        
        # Join emojis in this row without spaces
        message_rows.append(''.join(row_emojis))
    
    # Join all rows with newlines
    return '\n'.join(message_rows)

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



@bot.tree.command(name="write", description="Convert your message to powerline!")
async def message(interaction: discord.Interaction, text: str):
    """
    Convert text to powerline emoji
    Args:
        text: The text to convert
    """
    if not text.strip():
        await interaction.response.send_message("Please enter some text!", ephemeral=True)
        return

    # Check character limit
    if len(text) > 3:
        await interaction.response.send_message("Please enter no more than 3 characters!", ephemeral=True)
        return

    # Check if all characters are supported
    invalid_chars = [char for char in text if char not in LETTER_PATTERNS["LETTER_PATTERNS"]]
    
    if invalid_chars:
        unique_invalid = ', '.join(set(invalid_chars))
        await interaction.response.send_message(f"Sorry, I can't convert {unique_invalid} into powerline", ephemeral=True)
        return

    if contains_swearword(text):
        responses = [
            "Stop fucking swearing you shit head",
            "Nice try!",
            "Hey, no swearing!"
        ]
        await interaction.response.send_message(random.choice(responses), ephemeral=True)
        return

    # Process text in groups of 3 characters
    for i in range(0, len(text), 3):
        character_group = text[i:i+3]
        emoji_message = convert_characters_to_emoji(character_group)
        
        # Send the emoji message
        if i == 0:
            await interaction.response.send_message(emoji_message)
        else:
            await interaction.channel.send(emoji_message)


# Run the bot
bot.run(os.getenv('DISCORD_TOKEN'))