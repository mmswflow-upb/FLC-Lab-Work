import csv

# Task 1: Create HTML with Ordered and Unordered List
def create_list_html():
    # Read names and emails from a CSV file
    csv_file = 'Lab7.csv'  # Replace with the actual file path
    names = []
    emails = []

    try:
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                names.append(row['FirstName'])
                emails.append(row['Email'])
    except FileNotFoundError:
        print("CSV file not found. Ensure 'Lab7.csv' exists in the same directory.")
        return

    # Define colors for list items
    colors = ["red", "blue", "green", "purple", "brown", "orange", "pink", "cyan", "lime", "magenta"]

    # Create HTML content
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>HTML Lists</title>
    </head>
    <body style="background-color: lightgray;">
        <h1>Ordered and Unordered Lists</h1>
        <h2>Ordered List</h2>
        <ol>
    """
    for email, color in zip(emails, colors * (len(emails) // len(colors) + 1)):
        html_content += f'<li style="color: {color};">{email}</li>\n'

    html_content += """
        </ol>
        <h2>Unordered List</h2>
        <ul>
    """
    for name, color in zip(names, colors * (len(names) // len(colors) + 1)):
        html_content += f'<li style="color: {color};">{name}</li>\n'

    html_content += """
        </ul>
    </body>
    </html>
    """

    # Write HTML to a file
    with open("list.html", "w") as file:
        file.write(html_content)

    print("list.html created successfully!")


# Task 2: Create HTML Table
def create_table_html():
    # Data
    names = ["Alex", "Emma", "Kate", "Ryan", "Lily"]
    ages = [21, 25, 36, 31, 27]

    # Create HTML content
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>HTML Table</title>
    </head>
    <body style="background-color: lightblue;">
        <h1>Table of Names and Ages</h1>
        <table border="1" style="width:50%; text-align:center; border-collapse:collapse;">
            <tr>
                <th>Name</th>
                <th>Age</th>
            </tr>
    """
    for name, age in zip(names, ages):
        html_content += f"""
            <tr>
                <td>{name}</td>
                <td>{age}</td>
            </tr>
        """

    html_content += """
        </table>
    </body>
    </html>
    """

    # Write HTML to a file
    with open("table.html", "w") as file:
        file.write(html_content)

    print("table.html created successfully!")


# Main Function to Execute Both Tasks
if __name__ == "__main__":
    create_list_html()
    create_table_html()
