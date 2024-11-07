from player import Player
from playerservice import PlayerService, SortBy

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    service = PlayerService(url=url)

    print("Oliot:")
    players = service.players_by_nationality("FIN")
    sorted_players = service.sort_players(players, SortBy.POINTS)

    for player in sorted_players:
        print(player)


if __name__ == "__main__":
    main()
