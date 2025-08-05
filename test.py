import re

def split_string_into_components(input_string):
    # This pattern matches multiple time components in HH:M or HH:MM format and a number that follows them
    pattern = r'((?:\d{1,2}:\d{1,2}\s*(?:och|and)?\s*)*\d{1,2}:\d{1,2})\s*(\d+)'
    match = re.search(pattern, input_string)

    if match:
        times_part = match.group(1)
        # Split by "och" or "and" to handle different languages
        time_components = [t.strip() for t in re.split(r'\s*(?:och|and)\s*', times_part)]

        number_component = int(match.group(2))

        # Extract the remaining text before the times
        remaining_text = input_string[:match.start()].strip()

        return time_components, number_component, remaining_text
    else:
        return [], None, input_string

# Test the function with all three examples
examples = [
    "Kävlingevägen 101. Vallkärra 5:32  10",
    "Kävlingevägen 107. Vallkärra 12:1, 28:1 och 19:1 Kyrkan  3",
    "Vallkärra 284. Vallkärra 5:18 och 5:35, Villa Walhall  83",
    "Rönnströms väg 2 och 6. Vallkärrtorn 4:5 och 4:10. Tores Hage	61"
]

for example in examples:
    output = split_string_into_components(example)
    print(f"Input: {example}")
    print(f"Output: {output}\n")
