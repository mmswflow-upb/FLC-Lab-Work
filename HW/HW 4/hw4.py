import re
import pandas as pd

def parse_html_with_regex(file_path):
    with open(file_path, 'r') as file:
        html_content = file.read()

    links = re.findall(r'href="(https?://[^"]+)"', html_content)
    print("Links:", links)

    labels = re.findall(r'<label[^>]*>(.*?)</label>', html_content)
    print("Labels:", labels)

    input_types = re.findall(r'<input[^>]*type="([^"]+)"', html_content)
    print("Input Types:", input_types)

    options = re.findall(r'<option[^>]*>(.*?)</option>', html_content)
    print("Options:", options)

    ids = re.findall(r'id="([^"]+)"', html_content)
    print("IDs:", ids)

def convert_txt_to_excel(txt_file_path, excel_file_path):
    pattern = r"(\w+)\s*,\s*(\w+)\s*,\s*(\d{4}-\d{2}-\d{2})\s*,\s*(\d+)"

    last_names = []
    first_names = []
    hiring_dates = []
    salaries = []

    # Read the file and apply the regex pattern
    with open(txt_file_path, "r") as file:
        for line in file:
            match = re.match(pattern, line)
            if match:
                last_names.append(match.group(1))
                first_names.append(match.group(2))
                hiring_dates.append(match.group(3))
                salaries.append(int(match.group(4)))  # Convert salary to integer

    # Create a DataFrame from the extracted data
    df = pd.DataFrame({
        "LastName": last_names,
        "FirstName": first_names,
        "HiringDate": hiring_dates,
        "Salary": salaries
    })

    # Save the DataFrame to an Excel file
    df.to_excel(excel_file_path, index=False)
    print(f"Excel file created: {excel_file_path}")

# Exercise 3: Regex to Check HTML Tag Consistency
def check_html_tags(tag_list):
    # Function to check if HTML tags are correctly written
    pattern = r"<\s*/?\s*\w+\s*/?\s*>"
    results = {tag: bool(re.fullmatch(pattern, tag)) for tag in tag_list}
    print("Tag Consistency Results:", results)

def dfa_ab_language(word):
    states = {
        'start': {'a': 'state_a', 'b': 'reject'}, 
        'state_a': {'a': 'reject', 'b': 'accept_start'},  
        'before_last': {'a': 'before_last_a', 'b': 'accept_end'},  
        'before_last_a': {'a': 'reject', 'b': 'accept_end'},
    }

    current_state = 'start'
    
    for char in word:
        if current_state == 'accept_start': 
            continue
        elif current_state in states and char in states[current_state]:
            current_state = states[current_state][char]
        else:
            current_state = 'reject'
            break
    
    if len(word) >= 2 and word[-2:] == "ab":
        current_state = 'accept_end'
    
    # Determine acceptance
    return current_state in ('accept_start', 'accept_end')

def check_dfa_examples(words):
    results = {word: dfa_ab_language(word) for word in words}
    print("DFA Language Results:", results)

def main():
    parse_html_with_regex("HW5Ex1.html")
    
    convert_txt_to_excel("HW5Ex2.txt", "HW5Ex2.xlsx")

    tags = ["<p>", "< p >", "<p/>", "< /p>", "< id >", "<p>"]
    check_html_tags(tags)

    words = ["abaa", "aabab", "aabba", "ab", "abab", "aabb"]
    check_dfa_examples(words)

if __name__ == "__main__":
    main()
