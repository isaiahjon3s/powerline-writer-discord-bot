# Emoji definitions for Discord emoji IDs
EMOJIS = {
    'vl': '<:vl:1376092834356006954>',
    'hl': '<:hl:1376092817444835339>',
    'gd': '<:gd:1376092783458123796>',
    'l1': '<:l1:1376086874401144885>',
    'l2': '<:l2:1376086853689540639>',
    'l3': '<:l3:1376086831166263317>',
    'l4': '<:l4:1376086803865407520>',
    't1': '<:t1:1376264977848995840>',
    't2': '<:t2:1376265050280693891>',
    't3': '<:t3:1376265090424373408>',
    't4': '<:t4:1376265149085647009>',
    'i1': '<:i1:1376093284258156606>',
    'i2': '<:i2:1376093263249014795>',
    'i3': '<:i3:1376093303208153169>',
    'i4': '<:i4:1376093242596130887>',
    'h1': '<:h1:1376093217149288448>',
    'h2': '<:h2:1376093199571091496>',
    'h3': '<:h3:1378075677907226696>',
    'h4': '<:h4:1376093179295694901>',
    'x1': '<:x1:1376265190038966312>'
}

def get_emoji(name: str) -> str:
    """
    Get an emoji by its name.
    Args:
        name: The name of the emoji
    Returns:
        The emoji string
    """
    return EMOJIS.get(name, name)