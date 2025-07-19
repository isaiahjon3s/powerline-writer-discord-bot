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


# Interactive usage:
if __name__ == "__main__":
    get_emoji()