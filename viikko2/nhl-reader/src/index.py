from player_reader import PlayerReader
from player_stats import PlayerStats
from player import Player
from ui import UI

from datetime import datetime

def main():
    ui = UI()

    current_year = datetime.now().year
    default = f"{current_year}-{current_year-1999}"

    season = ui.ask_season(default)
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"

    service = PlayerReader(url=url)
    stats = PlayerStats(service)

    nat = ui.ask_nationality(default="FIN")

    players = stats.top_scorers_by_nationality(nat)

    ui.print_table(players, nat, season)


if __name__ == "__main__":
    main()
