# Discord Emoji Message Bot

This Discord bot converts text messages into emoji representations using a slash command.

## Setup

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file in the root directory and add your Discord bot token:
```
DISCORD_TOKEN=your_bot_token_here
```

3. Run the bot:
```bash
python bot.py
```

## Usage

Use the `/message` slash command followed by your text to convert it to emojis. For example:
```
/message Hello World!
```

This will convert the text into emoji representations.

## Features

- Converts text to emoji representations
- Supports letters, spaces, and basic punctuation
- Uses slash commands for easy interaction 