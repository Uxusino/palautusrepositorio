import requests
from player import Player
from enum import Enum

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3

class PlayerService:
    def __init__(self, url: str):
        self._response = requests.get(url).json()

    def players_by_nationality(self, nat):
        players = []

        for player_dict in self._response:
            player = Player(player_dict)
            if player.nationality == nat:
                players.append(player)

        return players
    
    def sort_players(self, players: list, sortby: SortBy):
        def sort(player: Player):
            if sortby == SortBy.POINTS:
                return player.points
            if sortby == SortBy.GOALS:
                return player.goals
            if sortby == SortBy.ASSISTS:
                return player.assists
            return player.points

        sorted_players = sorted(
            players,
            reverse=True,
            key=sort
        )

        return sorted_players