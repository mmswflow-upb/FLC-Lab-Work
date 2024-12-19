import re

def replace_capital_and_digits(input_file, output_file):
    # Regular expression for words containing only capital letters and/or digits
    pattern = re.compile(r'\b[A-Z0-9]+\b')

    try:
        # Read the input file
        with open(input_file, 'r') as infile:
            content = infile.read()

        # Replace matching words with $
        replaced_content = pattern.sub('$', content)

        # Save the modified content to the output file
        with open(output_file, 'w') as outfile:
            outfile.write(replaced_content)

        print(f"Replaced words saved to {output_file}")
    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_file = "ex4_in.txt"
output_file = "ex4_out.txt"
replace_capital_and_digits(input_file, output_file)
