import re

def find_and_save_urls(input_file, output_file):
    url_pattern = re.compile(r'\bhttps?://(?:[a-zA-Z0-9-]+\.)?[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(?:/\S*)?\b')

    try:
        # Read the input file
        with open(input_file, 'r') as infile:
            content = infile.read()

        urls = url_pattern.findall(content)

        with open(output_file, 'w') as outfile:
            for url in urls:
                outfile.write(url + '\n')

        print(f"Found and saved {len(urls)} URLs to {output_file}")
    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_file = "ex4_in.txt"
output_file = "ex4_out.txt"
find_and_save_urls(input_file, output_file)
