# Discord Power Writing Bot

A Discord bot that converts text into powerline using custom emoji patterns. The bot reads letter patterns from a JSON file and converts them into Discord emoji messages with built-in swearword filtering.

## Features

- Convert text (up to 3 characters) to powerline emoji writing
- Built-in swearword detection with evasion protection with log system for moderators
- Configurable character substitutions for robust filtering
- Support for all letters and common characters

## Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file with your Discord bot token and moderation message log channel id:
   ```
   DISCORD_TOKEN=your_token_here
   MOD_MESSAGE_LOG_CHANNEL_ID=your_channel_id_here
   ```
4. Run the bot:
   ```bash
   python3 bot.py
   ```

## Commands

- `/write <text>` - Convert text to emoji art (max 3 characters)

## Configuration Files

- `letter_patterns.json` - Defines emoji patterns for each character
- `swearwords.json` - List of words to filter out
- `substitutions.json` - Character substitution patterns for evasion detection
- `emoji_config.py` - Maps emoji names to Discord emoji IDs

## How It Works

1. User types `/write <text>` (max 3 characters)
2. Bot validates characters against available patterns
3. Bot checks for swearwords (including evasion attempts)
4. Bot converts each character to 6-line emoji art patterns
5. Bot sends the formatted emoji message
