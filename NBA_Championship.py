import requests
from bs4 import BeautifulSoup
from collections import Counter

# Wikipedia URL for NBA champions
URL = "https://en.wikipedia.org/wiki/List_of_NBA_champions"

# Fetch the webpage
response = requests.get(URL)
if response.status_code != 200:
    print("Failed to retrieve the webpage")
    exit()

# Parse the webpage content
soup = BeautifulSoup(response.text, "html.parser")

# Find the main table containing championship data
table = soup.find("table", {"class": "wikitable"})
if not table:
    print("Could not find the required table on the page")
    exit()

# Extract all rows from the table
rows = table.find_all("tr")[1:]

# Dictionary to count championships by team
team_wins = Counter()

for row in rows:
    columns = row.find_all("td")
    if len(columns) < 4:
        continue  # Skip rows without enough columns

    winner = columns[1].get_text(strip=True)
    team_wins[winner] += 1

# Sort teams by the number of championships won
top_teams = sorted(team_wins.items(), key=lambda x: x[1], reverse=True)[:20]

# Output the top 20 teams
print("Top 20 NBA Championship-winning Teams:")
for rank, (team, wins) in enumerate(top_teams, 1):
    print(f"{rank}. {team} - {wins} titles")

if __name__ == "__main__":
    fetch_nba_champions()