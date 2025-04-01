#https://en.wikipedia.org/wiki/List_of_NBA_champions

import requests
from bs4 import BeautifulSoup
from collections import Counter

URL = "https://en.wikipedia.org/wiki/List_of_NBA_champions"

response = requests.get(URL)
if response.status_code != 200:
    print("Failed to retrieve the webpage")
    exit()


soup = BeautifulSoup(response.text, "html.parser")

table = soup.find("table", {"class": "wikitable"})
if not table:
    print("Could not find the required table on the page")
    exit()

rows = table.find_all("tr")[1:]


team_wins = Counter()

for row in rows:
    columns = row.find_all("td")
    if len(columns) < 4:
        continue  # Skip rows without enough columns

    winner = columns[1].get_text(strip=True)
    team_wins[winner] += 1

top_teams = sorted(team_wins.items(), key=lambda x: x[1], reverse=True)[:20]

print("Top 20 NBA Championship-winning Teams:")
for rank, (team, wins) in enumerate(top_teams, 1):
    print(f"{rank}. {team} - {wins} titles")

if __name__ == "__main__":
    fetch_NBA_championship_()