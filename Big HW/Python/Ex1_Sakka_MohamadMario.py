import re

def to_snake_case(text):
    text = re.sub(r'\s+', '_', text)  
    snake_case = re.sub(r'(?<!_)([A-Z])', r'_\1', text)  
    return snake_case.strip('_').lower()  

examples = [
    "Hello NewWorld",
    "Convert this String To Snake Case",
    "Python Program Example",
    "SnakeCase Example For Testing"
]

for example in examples:
    print(f"Original: {example}")
    print(f"Snake Case: {to_snake_case(example)}\n")
