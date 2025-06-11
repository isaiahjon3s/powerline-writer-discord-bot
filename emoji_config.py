# Emoji definitions
EMOJIS = {
    'vl': ('<:vl:1376092834356006954>', 2),
    'hl': ('<:hl:1376092817444835339>', 2),
    'gd': ('<:gd:1376092783458123796>', 0),
    'l1': ('<:l1:1376086874401144885>', 2),
    'l2': ('<:l2:1376086853689540639>', 2),
    'l3': ('<:l3:1376086831166263317>', 2),
    'l4': ('<:l4:1376086803865407520>', 2),
    't1': ('<:t1:1376264977848995840>', 2),
    't2': ('<:t2:1376265050280693891>', 3),
    't3': ('<:t3:1376265090424373408>', 3),
    't4': ('<:t4:1376265149085647009>', 3),
    'i1': ('<:i1:1376093284258156606>', 1),
    'i2': ('<:i2:1376093263249014795>', 1),
    'i3': ('<:i3:1376093303208153169>', 1),
    'i4': ('<:i4:1376093242596130887>', 1),
    'h1': ('<:h1:1376093217149288448>', 1),
    'h2': ('<:h2:1376093199571091496>', 1),
    'h3': ('<:h3:1378075677907226696>', 1),  
    'h4': ('<:h4:1376093179295694901>', 1),
    'x1': ('<:x1:1376265190038966312>', 4)
}

# Create reverse mapping for emoji conversion
REVERSE_EMOJIS = {value: key for key, value in EMOJIS.items()}

def get_emoji(name: str) -> str:
    """
    Get an emoji by its name.
    Args:
        name: The name of the emoji
    Returns:
        The emoji string
    """
    return EMOJIS.get(name, name)[0]  # Return just the emoji string, not the length

def convert_emoji_string(input_string: str) -> str:
    """
    Convert a string containing Discord emoji format to custom emoji names.
    Args:
        input_string: String containing emojis in format <:emoji:ID>
    Returns:
        String with emojis converted to custom names
    """
    # Find all emoji patterns in the string
    converted_parts = []
    current_pos = 0
    
    while current_pos < len(input_string):
        # Find the next <
        start = input_string.find('<', current_pos)
        if start == -1:
            break
            
        # Find the next >
        end = input_string.find('>', start)
        if end == -1:
            break
            
        # Extract the emoji part
        emoji_part = input_string[start:end+1]
        
        # Remove < and >
        emoji_part = emoji_part.strip('<>')
        
        # Extract the emoji name (between the colons)
        if ':' in emoji_part:
            emoji_parts = emoji_part.split(':')
            if len(emoji_parts) >= 2:
                emoji_name = emoji_parts[1]  # Get the name between colons
                # Get the custom name from our reverse mapping
                custom_name = REVERSE_EMOJIS.get(f":{emoji_name}:", emoji_name)
                converted_parts.append(custom_name)
        
        current_pos = end + 1
    
    return ' '.join(converted_parts)

# Interactive usage:
if __name__ == "__main__":
    print("Enter your emoji string (type 'quit' to exit):")
    while True:
        user_input = input("> ")
        if user_input.lower() == 'quit':
            break
        converted = convert_emoji_string(user_input)
        print(f"Converted: {converted}")
        print()


# Function to get a random emoji for a letter
def get_emoji_for_letter(letter: str, index: int = 0) -> str:
    """
    Get an emoji for a given letter.
    Args:
        letter: The letter to get an emoji for
        index: Which emoji to use (0-3)
    Returns:
        The emoji string
    """
    letter = letter.lower()
    if letter in LETTER_FORMATS:
        emojis = LETTER_FORMATS[letter]
        emoji = emojis[index % len(emojis)]
        # Convert 'vl' to the actual emoji
        if emoji == 'vl':
            return ':vl:'
        return emoji
    return letter

# Function to get all emojis for a letter
def get_all_emojis_for_letter(letter: str) -> list:
    """
    Get all emojis for a given letter.
    Args:
        letter: The letter to get emojis for
    Returns:
        List of all emojis for that letter
    """
    letter = letter.upper()  # Convert to uppercase since patterns are in uppercase
    if letter not in LETTER_PATTERNS["LETTER_PATTERNS"]:
        return [letter]
    
    # Get all emojis from all lines
    emojis = []
    for line in LETTER_PATTERNS["LETTER_PATTERNS"][letter].values():
        emojis.extend(line)
    
    # Convert to actual emoji strings
    return [get_emoji(emoji) for emoji in emojis]

def get_longest_letter(letters: str) -> str:
    """
    Determine which letter in the input has the longest emoji representation.
    Args:
        letters: String of letters to check (should be 3 letters)
    Returns:
        The letter with the longest emoji representation
    """
    if len(letters) != 3:
        raise ValueError("Input must be exactly 3 letters")
    
    max_length = 0
    longest_letter = letters[0]
    
    for letter in letters:
        letter = letter.upper()  # Convert to uppercase since patterns are in uppercase
        if letter in LETTER_PATTERNS["LETTER_PATTERNS"]:
            # Get all lines for this letter
            letter_pattern = LETTER_PATTERNS["LETTER_PATTERNS"][letter]
            # Find the maximum length among all emojis in all lines
            letter_length = max(
                EMOJIS[emoji][1] 
                for line in letter_pattern.values() 
                for emoji in line 
                if emoji in EMOJIS
            )
            if letter_length > max_length:
                max_length = letter_length
                longest_letter = letter
    
    return longest_letter 