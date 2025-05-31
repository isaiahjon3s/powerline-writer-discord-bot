# Discord Power Writing Bot

A Discord bot that converts text into emoji art using custom emoji patterns. The bot reads letter patterns from a JSON file and converts them into Discord emoji messages.

## Features

- Convert text to emoji art using custom emoji patterns
- Support for multiple characters
- Automatic message splitting for long text
- Show available emojis for specific letters

## Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file with your Discord bot token:
   ```
   DISCORD_TOKEN=your_token_here
   ```
4. Run the bot:
   ```bash
   python bot.py
   ```

## Commands

- `/message <text>` - Convert text to emoji art
- `/show_emojis <letter>` - Show all available emojis for a specific letter

## File Structure

- `bot.py` - Main bot code
- `emoji_config.py` - Emoji configuration and helper functions
- `letter_patterns.json` - JSON file containing letter patterns
- `.env` - Environment variables (not tracked in git)
- `requirements.txt` - Python dependencies

## License

MIT License 