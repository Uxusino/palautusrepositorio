from player_reader import PlayerReader
from enum import Enum

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3

class StatisticsService:
    def __init__(self, reader: PlayerReader):

        self._players = reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many, sortby: SortBy = SortBy.POINTS):
        # metodin käyttämä apufufunktio voidaan määritellä näin
        def sort(player):
            if sortby == SortBy.POINTS:
                return player.points
            if sortby == SortBy.GOALS:
                return player.goals
            if sortby == SortBy.ASSISTS:
                return player.assists
            return player.points

        sorted_players = sorted(
            self._players,
            reverse=True,
            key=sort
        )

        result = []
        i = 0
        # Changed from "how_many" to "how_many-1", because it's more logical to type "top(5)"
        # and get top 5 players than type "top(4)" to get top 5 players because list index is out of range
        while i <= how_many-1:
            result.append(sorted_players[i])
            i += 1

        return result
