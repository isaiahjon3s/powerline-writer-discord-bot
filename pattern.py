import json

def translate_pattern(pattern_part):
    """Convert k1-k4 to h1-h4 and strip colons."""
    if pattern_part.startswith('k'):
        num = pattern_part[1:]
        return f'h{num}'
    return pattern_part

def parse_input(input_text):
    """Split input into lines and process each line."""
    lines = input_text.strip().split('\n')
    if len(lines) != 6:
        raise ValueError("Input must have exactly 6 lines.")
    
    processed_lines = []
    for line in lines:
        # Remove leading/trailing colons and split
        parts = line.strip(':').split('::')
        if len(parts) != 4:
            raise ValueError(f"Each line must have exactly 4 parts. Got: {line}")
        processed_line = [translate_pattern(part) for part in parts]
        processed_lines.append(processed_line)
    
    return processed_lines

def create_letter_pattern(letter, processed_lines):
    """Generate the JSON structure."""
    return {
        "LOWERCASE_LETTER_PATTERNS": {
            letter: {
                "line_1": processed_lines[0],
                "line_2": processed_lines[1],
                "line_3": processed_lines[2],
                "line_4": processed_lines[3],
                "line_5": processed_lines[4],
                "line_6": processed_lines[5]
            }
        }
    }

def main():
    print("Enter the letter you're defining (e.g., 'a'): ")
    letter = input().strip().lower()
    
    print("Paste all 6 lines at once (each line with 4 colon-separated parts):")
    input_lines = []
    for _ in range(6):
        line = input().strip()
        input_lines.append(line)
    input_text = '\n'.join(input_lines)
    
    processed_lines = parse_input(input_text)
    result = create_letter_pattern(letter, processed_lines)
    
    print("\nOutput:")
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()