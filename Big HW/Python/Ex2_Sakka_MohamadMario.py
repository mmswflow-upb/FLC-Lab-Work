import re

def process_string(input_string):
    switched_case = ''.join([char.lower() if char.isupper() else char.upper() for char in input_string])
    print(f"Step 1 - Case switched: {switched_case}")

    lowercase_only = re.sub(r'[A-Z]', '', switched_case)
    print(f"Step 2 - Uppercase letters removed: {lowercase_only}")

examples = ["StuDeNT", "PyThoN", "RegEx", "CompuTer"]

for i, example in enumerate(examples, 1):
    print(f"\nExample {i}: Input string: {example}")
    process_string(example)
