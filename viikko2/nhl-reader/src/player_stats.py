from player_reader import PlayerReader
from player import Player
from enum import Enum

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3

class PlayerStats:
    def __init__(self, reader: PlayerReader):
        self._reader = reader

    def top_scorers_by_nationality(self, nat: str):
        players = []

        for player in self._reader.players:
            if player.nationality == nat:
                players.append(player)

        sorted_players = self.sort_players(players, SortBy.POINTS)

        return sorted_players
    
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