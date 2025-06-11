# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re
import json

def load_swearwords():
    with open('swearwords.json', 'r') as f:
        data = json.load(f)
        return data['SWEARWORDS']

def contains_swearword(text):
    """
    Check if the given text contains any swear words or bypass attempts.
    Returns True if a swear word or bypass is found, False otherwise.
    """
    swearwords = load_swearwords()
    text_lower = text.lower()
    
    # Create a pattern that matches words with common character substitutions
    pattern = r'\b(' + '|'.join(
        re.escape(word).replace('a', '[a@4]')
                       .replace('e', '[e3]')
                       .replace('i', '[i1!l]')
                       .replace('o', '[o0]')
                       .replace('s', '[s$5z]')
                       .replace('t', '[t7]')
                       .replace('u', '[uv]')
                       .replace('g', '[g9]')
                       .replace('l', '[i1!]')
                       .replace('c', '[ck]')
        for word in swearwords
    ) + r')\b'
    
    # First check for exact matches
    if re.search(pattern, text_lower, re.IGNORECASE):
        return True
        
    # Then check for specific bypass attempts
    bypass_pattern = r'\b(' + '|'.join(
        re.escape(word).replace('i', '[i1!]').replace('l', '[l1]')
        for word in swearwords
    ) + r')\b'
    
    matches = re.finditer(bypass_pattern, text_lower, re.MULTILINE | re.IGNORECASE)
    
    for matchNum, match in enumerate(matches, start=1):
        print(f"Match {matchNum} was found at {match.start()}-{match.end()}: {match.group()}")
        
        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1
            print(f"Group {groupNum} found at {match.start(groupNum)}-{match.end(groupNum)}: {match.group(groupNum)}")
    
    return bool(re.search(bypass_pattern, text_lower, re.IGNORECASE))

# Test the function
if __name__ == "__main__":
    test_words = load_swearwords()
    print("Loaded swear words:", test_words)
    

    
    for test in test_cases:
        result = contains_swearword(test)
        print(f"Testing '{test}': {'Contains swear word' if result else 'Clean'}")
