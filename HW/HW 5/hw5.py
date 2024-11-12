import requests
from bs4 import BeautifulSoup
import openpyxl

# URL of the website to scrape
url = "https://www.scrapethissite.com/pages/simple/"

# Send a request to fetch the page content
response = requests.get(url)
response.raise_for_status()  # Check if the request was successful

# Parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Create an Excel workbook and sheet
wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = "Countries Data"
sheet.append(["CountryName", "Capital", "Population", "Area"])

# Extract country data
countries = soup.find_all("div", class_="col-md-4 country")
for country in countries:
    # Extract the country details
    country_name = country.find("h3", class_="country-name").get_text(strip=True)
    capital = country.find("span", class_="country-capital").get_text(strip=True)
    population = country.find("span", class_="country-population").get_text(strip=True)
    area = country.find("span", class_="country-area").get_text(strip=True)

    # Append data to the Excel sheet
    sheet.append([country_name, capital, population, area])

# Extract links based on specific IDs
link_ids = {
    "Sandbox": "nav-sandbox",
    "Lessons": "nav-lessons",
    "FAQ": "nav-faq",
    "Login": "nav-login"
}
links_sheet = wb.create_sheet(title="Links")
links_sheet.append(["Link Name", "URL"])

for name, link_id in link_ids.items():
    link_tag = soup.find("li", id=link_id)
    link_url = link_tag.find("a")["href"] if link_tag and link_tag.find("a") else "Link not found"
    links_sheet.append([name, link_url])

# Function to recursively extract text from a given tag
def get_footer_text(tag):
    if tag.string:  # Direct text found
        return tag.string.strip()
    for child in tag.children:  # Loop through all child tags
        result = get_footer_text(child)
        if result:  # Stop when actual text is found
            return result
    return None

# Find footer section and extract text
footer_section = soup.find(id="footer")
footer_text = get_footer_text(footer_section) if footer_section else "Footer not found"
links_sheet.append(["Footer Text", footer_text])

# Save the workbook
wb.save("countries_and_links_data.xlsx")
print("Data has been saved to countries_and_links_data.xlsx")
