from player import Player

from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

SEASONS = [
    "2018-19",
    "2019-20",
    "2020-21",
    "2021-22",
    "2022-23",
    "2023-24",
    "2024-25"
]

NATIONALITIES = ["AUT", "CZE", "AUS",
                 "SWE", "GER", "DEN",
                 "SUI", "SVK", "NOR",
                 "RUS", "CAN", "LAT",
                 "BLR", "SLO", "USA",
                 "FIN", "GBR"]

class UI:
    def __init__(self):
        self._console = Console()

    def print_table(self, players: list[Player], nationality: str, season: str):
        table = Table(title=f"Top players of {nationality} season {season}")

        table.add_column("name", style="cyan")
        table.add_column("team", style="magenta")
        table.add_column("goals", style="green")
        table.add_column("assists", style="green")
        table.add_column("points", style="green")

        if len(players) == 0:
                table.add_row("No", "one", "lol", ":--", "DDD")
        else:
            for player in players:
                table.add_row(player.name, player.team, str(player.goals), str(player.assists), str(player.points))
        
        self._console.print(table)

    def ask_season(self, default: str = None):
        season = Prompt.ask("Select season", choices=SEASONS, default=default)
        return season
    
    def ask_nationality(self, default: str = None):
        nat = Prompt.ask("Select nationality", choices=NATIONALITIES, default=default)
        return nat