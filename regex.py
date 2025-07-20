# Enhanced swearword detection with regex patterns to catch character substitutions
# Uses substitutions.json for configurable character mappings

import re
import json

# Cache for substitutions and compiled regex patterns
_substitutions_cache = None
_regex_pattern_cache = None

def load_substitutions():
    """
    Load character substitutions from substitutions.json
    Returns:
        dict: Dictionary mapping characters to their substitution patterns
    """
    global _substitutions_cache
    
    if _substitutions_cache is not None:
        return _substitutions_cache
    
    try:
        with open('substitutions.json', 'r') as f:
            data = json.load(f)
        _substitutions_cache = data.get('SUBSTITUTIONS', {})
        return _substitutions_cache
    except (FileNotFoundError, json.JSONDecodeError, KeyError):
        print("Failed to load substitutions.json")
        _substitutions_cache = {}
        return {}

def create_evasion_pattern(word):
    """
    Create a regex pattern that matches the word with common character substitutions
    Args:
        word (str): The original word
    Returns:
        str: Regex pattern that matches the word with substitutions
    """
    substitutions = load_substitutions()
    
    pattern = ''
    for char in word.lower():
        if char in substitutions:
            pattern += substitutions[char]
        else:
            pattern += re.escape(char)
    
    return rf'\b{pattern}\b'

def get_compiled_regex():
    """
    Get or create the compiled regex pattern for swearword detection
    Returns:
        re.Pattern: Compiled regex pattern
    """
    global _regex_pattern_cache
    
    if _regex_pattern_cache is not None:
        return _regex_pattern_cache
    
    try:
        with open('swearwords.json', 'r') as f:
            swearwords_data = json.load(f)
        
        swearwords = swearwords_data.get('SWEARWORDS', [])
        patterns = [create_evasion_pattern(word) for word in swearwords]
        combined_pattern = '|'.join(patterns)
        
        _regex_pattern_cache = re.compile(combined_pattern, re.IGNORECASE)
        return _regex_pattern_cache
        
    except (FileNotFoundError, json.JSONDecodeError, KeyError):
        # Return a pattern that matches nothing
        _regex_pattern_cache = re.compile(r'(?!.*)', re.IGNORECASE)
        return _regex_pattern_cache

def contains_swearword(text):
    """
    Check if the given text contains any swearwords from swearwords.json
    Uses regex patterns to catch common character substitutions
    Args:
        text (str): The text to check
    Returns:
        bool: True if text contains a swearword, False otherwise
    """
    regex = get_compiled_regex()
    return bool(regex.search(text))

