import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

def scrape_table_data(base_url):
    all_rows = []  
    headers = None  
    
    response = requests.get(base_url)
    if response.status_code != 200:
        print(f"Failed to fetch page. Status code: {response.status_code}")
    
    soup = BeautifulSoup(response.content, "html.parser")
    
    table = soup.find("table", {"class": "table"})
    if not table:
        print(f"No table found on page. Stopping.")
    
    if headers is None:
        header_row = table.find("tr")
        headers = [th.text.strip() for th in header_row.find_all("th")]
        if not headers:
            raise ValueError("Table headers not found.")

    for tr in table.find_all("tr", {"class": "team"}):
        cells = [td.text.strip() for td in tr.find_all("td")]
        if cells:  
            all_rows.append(cells)
    
    
    
    df = pd.DataFrame(all_rows, columns=headers)
    return df

def export_data(df):
    df.to_csv("ex6_teams_data.csv", index=False)
    df.to_excel("ex6_teams_data.xlsx", index=False)
    print("Data exported to 'teams_data.csv' and 'teams_data.xlsx'.")

def filter_by_city(df):
   
    def extract_city(team_name):
        words = team_name.split()
        if len(words) >= 3:
           
            return " ".join(words[:2])
        elif len(words) == 2:
         
            return words[0]
        return None  

    df["City"] = df["Team Name"].apply(extract_city)
  
    grouped = df.groupby("City")["Team Name"].apply(lambda teams: list(set(teams)))
    
    print("\nTeams from the same city:\n", grouped)



def sort_by_wins(df):
    df["Wins"] = pd.to_numeric(df["Wins"], errors="coerce")
    sorted_df = df.sort_values(by="Wins", ascending=False)
    print("Teams sorted by Wins:\n", sorted_df[["Team Name", "Wins"]])

def extract_search_bar(soup):
    form = soup.find("form", {"class": "form form-inline"})
    if form:
        action = form.get("action", "No action found")
        input_name = form.find("input", {"type": "text"}).get("name", "No name found")
        placeholder = form.find("input", {"type": "text"}).get("placeholder", "No placeholder found")
        print("\nSearch Bar Details:")
        print(f"Form Action: {action}")
        print(f"Input Field Name: {input_name}")
        print(f"Placeholder: {placeholder}")
    else:
        print("\nSearch bar not found.")

def extract_final_section(soup):
    video_lessons = soup.find("a", href=True, string=re.compile("8 video lessons"))
    if video_lessons:
        print(f"\nVideo Lessons Link: https://www.scrapethissite.com{video_lessons['href']}")
    else:
        print("\nVideo Lessons Link: Not found.")
    
    data_source = soup.find("a", href=True, string=re.compile("http://www.opensourcesports.com/hockey/"))
    if data_source:
        print(f"Data Source Link: {data_source['href']}")
    else:
        print("Data Source Link: Not found.")

def extract_pagination(soup):
    pagination = soup.find("ul", {"class": "pagination"})
    if pagination:
        pages = [a.get("href") for a in pagination.find_all("a", href=True)]
        print("\nPagination Links:")
        for page in pages:
            print(f"{page}")
    else:
        print("\nPagination not found.")
    
    return len(pages)

if __name__ == "__main__":
    url = "https://www.scrapethissite.com/pages/forms/"


    extract_search_bar(BeautifulSoup(requests.get(url).content, "html.parser"))
    extract_final_section(BeautifulSoup(requests.get(url).content, "html.parser"))

    max_pages = extract_pagination(BeautifulSoup(requests.get(url).content, "html.parser"))

    df = scrape_table_data(url)
    print("Data scraped successfully.")
    
    export_data(df)
    
    filter_by_city(df)
    
    sort_by_wins(df)
