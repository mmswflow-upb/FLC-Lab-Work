import re

def to_snake_case(input_string):
    snake_case_string = re.sub(r'\s+', '_', input_string.strip()).lower()
    return snake_case_string

examples = [
    "Hello JavaScript",
    "Convert This String To Snake Case",
    "Python Program Example",
    "Make Sure To Test It"
]

for i, example in enumerate(examples, 1):
    result = to_snake_case(example)
    print(f"Example {i}: {example} -> {result}")
