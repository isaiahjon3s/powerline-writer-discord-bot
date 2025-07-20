# TODO: Implement swearwords.json with regex!!!

import re
import json

def contains_swearword(text):
    """
    Check if the given text contains any swearwords from swearwords.json
    Args:
        text (str): The text to check
    Returns:
        bool: True if text contains a swearword, False otherwise
    """
    try:
        # Load swearwords from JSON file
        with open('swearwords.json', 'r') as f:
            swearwords_data = json.load(f)
        
        # Get the list of swearwords
        swearwords = swearwords_data.get('SWEARWORDS', [])
        
        # Convert text to lowercase for case-insensitive matching
        text_lower = text.lower()
        
        # Check if any swearword is in the text
        for swearword in swearwords:
            if swearword.lower() in text_lower:
                return True
        
        return False
        
    except (FileNotFoundError, json.JSONDecodeError, KeyError):
        # If file doesn't exist or is invalid, return False
        return False

