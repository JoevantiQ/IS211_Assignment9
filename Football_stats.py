#NFL Player Stats - Touchdowns
#https://www.cbssports.com/nfl/stats/player/passing/nfl/regular/qualifiers/

import requests
from bs4 import BeautifulSoup


def fetch_nfl_passing_stats():
    url = "https://www.cbssports.com/nfl/stats/player/passing/nfl/regular/qualifiers/"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("Failed to retrieve data")
        return

    soup = BeautifulSoup(response.text, "html.parser")


    table = soup.find("table", class_="TableBase-table")
    if not table:
        print("Could not find the stats table on the page")
        return

    headers = [th.text.strip() for th in table.find_all("th")]


    players = []
    for row in table.find("tbody").find_all("tr")[:20]:  # Get top 20 players
        cols = row.find_all("td")
        if len(cols) < 5:
            continue

        name = cols[0].text.strip()
        position = cols[1].text.strip()
        team = cols[2].text.strip()
        touchdowns = cols[5].text.strip()  # Assuming the 6th column contains touchdowns

        players.append((name, position, team, touchdowns))

    print("Top 20 NFL Passing Leaders:")
    for player in players:
        print(f"{player[0]} ({player[1]}, {player[2]}) - TDs: {player[3]}")


if __name__ == "__main__":
    fetch_nfl_passing_stats()