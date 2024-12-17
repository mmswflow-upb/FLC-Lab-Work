import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

# 1. Scrape Table Data from the Page
def scrape_table_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    
    table = soup.find("table", {"class": "table"})
    headers = [th.text.strip() for th in table.find("thead").find_all("th")]
    
    rows = []
    for tr in table.find("tbody").find_all("tr"):
        cells = [td.text.strip() for td in tr.find_all("td")]
        rows.append(cells)
    
    return pd.DataFrame(rows, columns=headers)

# 2. Export Data to .xlsx and .csv
def export_data(df):
    df.to_csv("teams_data.csv", index=False)
    df.to_excel("teams_data.xlsx", index=False)
    print("Data exported to 'teams_data.csv' and 'teams_data.xlsx'.")

# 3. Filter Teams by City Name
def filter_by_city(df):
    df["City"] = df["Team Name"].apply(lambda name: " ".join(name.split()[:2]))  # Extract first two words
    grouped = df.groupby("City")["Team Name"].apply(list)
    print("Teams from the same city:\n", grouped)

# 4. Sort Teams by Wins
def sort_by_wins(df):
    df["Wins"] = pd.to_numeric(df["Wins"], errors="coerce")
    sorted_df = df.sort_values(by="Wins", ascending=False)
    print("Teams sorted by Wins:\n", sorted_df[["Team Name", "Wins"]])

# Main Execution
if __name__ == "__main__":
    url = "https://www.scrapethissite.com/pages/forms/"
    
    # Step 1: Scrape data
    df = scrape_table_data(url)
    print("Data scraped successfully.")
    
    # Step 2: Export to file
    export_data(df)
    
    # Step 3: Filter by city
    filter_by_city(df)
    
    # Step 4: Sort by wins
    sort_by_wins(df)
