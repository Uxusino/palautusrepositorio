import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search(self):
        player = self.stats.search("Semenko")

        self.assertEqual(str(player), str(Player("Semenko", "EDM", 4, 12)))

    def test_wrong_player(self):
        player = self.stats.search("Dybovsky")

        self.assertIsNone(player)

    def test_team(self):
        players = self.stats.team("EDM")
        players_list = [str(player) for player in players]
        compare = [str(Player("Semenko", "EDM", 4, 12)),
                   str(Player("Kurri",   "EDM", 37, 53)),
                   str(Player("Gretzky", "EDM", 35, 89))]

        self.assertEqual(players_list, compare)

    def test_sort_by_points_no_parameter(self):
        results = self.stats.top(5)
        result_list = [str(result) for result in results]
        compare = [str(Player("Gretzky", "EDM", 35, 89)),
                   str(Player("Lemieux", "PIT", 45, 54)),
                   str(Player("Yzerman", "DET", 42, 56)),
                   str(Player("Kurri",   "EDM", 37, 53)),
                   str(Player("Semenko", "EDM", 4, 12))]
        
        self.assertEqual(result_list, compare)

    def test_sort_by_points_parameter(self):
        results = self.stats.top(5, sortby=SortBy.POINTS)
        result_list = [str(result) for result in results]
        compare = [str(Player("Gretzky", "EDM", 35, 89)),
                   str(Player("Lemieux", "PIT", 45, 54)),
                   str(Player("Yzerman", "DET", 42, 56)),
                   str(Player("Kurri",   "EDM", 37, 53)),
                   str(Player("Semenko", "EDM", 4, 12))]
        
        self.assertEqual(result_list, compare)

    def test_sort_by_goals(self):
        results = self.stats.top(2, SortBy.GOALS)
        result_list = [str(result) for result in results]
        compare = [str(Player("Lemieux", "PIT", 45, 54)),
                   str(Player("Yzerman", "DET", 42, 56))]
        
        self.assertEqual(result_list, compare)

    def test_sort_by_assists(self):
        results = self.stats.top(2, SortBy.ASSISTS)
        result_list = [str(result) for result in results]
        compare = [str(Player("Gretzky", "EDM", 35, 89)),
                   str(Player("Yzerman", "DET", 42, 56))]
        
        self.assertEqual(result_list, compare)

    def test_sort_wrong_method_defaults_to_points(self):
        results = self.stats.top(5, sortby=4)
        result_list = [str(result) for result in results]
        compare = [str(Player("Gretzky", "EDM", 35, 89)),
                   str(Player("Lemieux", "PIT", 45, 54)),
                   str(Player("Yzerman", "DET", 42, 56)),
                   str(Player("Kurri",   "EDM", 37, 53)),
                   str(Player("Semenko", "EDM", 4, 12))]
        
        self.assertEqual(result_list, compare)