import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

def search_team_data(team_name, base_url):
    response = requests.get(base_url, params={"q": team_name})
    soup = BeautifulSoup(response.content, "html.parser")

    table = soup.find("table", {"class": "table"})
    if not table:
        print("No table found for the given team.")
        return pd.DataFrame()

    header_row = table.find("tr")
    headers = [th.text.strip() for th in header_row.find_all("th")]

    # Extract rows
    rows = []
    for tr in table.find_all("tr", {"class": "team"}):
        cells = [td.text.strip() for td in tr.find_all("td")]
        if cells:
            rows.append(cells)

    df = pd.DataFrame(rows, columns=headers)
    print("Data successfully retrieved.")
    return df

def export_team_data(df, team_name):
    csv_filename = f"{team_name.replace(' ', '_').lower()}_data.csv"
    xlsx_filename = f"{team_name.replace(' ', '_').lower()}_data.xlsx"

    df.to_csv(csv_filename, index=False)
    df.to_excel(xlsx_filename, index=False)
    print(f"Data exported to '{csv_filename}' and '{xlsx_filename}'.")

def plot_team_performance(df, team_name):
    df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
    df["Wins"] = pd.to_numeric(df["Wins"], errors="coerce")
    df["Losses"] = pd.to_numeric(df["Losses"], errors="coerce")

    plt.figure(figsize=(8, 6))
    plt.bar(df["Year"] - 0.2, df["Wins"], width=0.4, label="Wins", color="magenta")
    plt.bar(df["Year"] + 0.2, df["Losses"], width=0.4, label="Losses", color="cyan")

    plt.title(f"{team_name} Wins/Losses")
    plt.xlabel("Year")
    plt.ylabel("Number")
    plt.xticks(df["Year"])
    plt.legend()
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()

    plot_filename = f"{team_name.replace(' ', '_').lower()}_wins_losses.png"
    plt.savefig(plot_filename)
    plt.show()
    print(f"Plot saved as '{plot_filename}'.")

if __name__ == "__main__":
    team_name = "Boston Bruins"
    base_url = "https://www.scrapethissite.com/pages/forms/"

    df = search_team_data(team_name, base_url)
    if not df.empty:
        print(df)

        export_team_data(df, team_name)

        plot_team_performance(df, team_name)
    else:
        print("No data to process.")
