LOVE = 0
FIFTEEN = 1
THIRTY = 2
FORTY = 3
GAME = 4

ALL_SCORES = {
    LOVE: "Love-All",
    FIFTEEN: "Fifteen-All",
    THIRTY: "Thirty-All",
    "deuce": "Deuce"
}

SCORES = {
    LOVE: "Love",
    FIFTEEN: "Fifteen",
    THIRTY: "Thirty",
    FORTY: "Forty"
}

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.m_score1 += 1
        if player_name == self.player2_name:
            self.m_score2 += 1

    def _count_equal_scores(self) -> str:
        if self.m_score1 in range(LOVE, THIRTY+1):
            score = ALL_SCORES[self.m_score1]
        else:
            score = ALL_SCORES["deuce"]
        return score
    
    def _count_minus_scores(self) -> str:
        minus_result = self.m_score1 - self.m_score2

        if minus_result == 1:
            score = f"Advantage {self.player1_name}"
        elif minus_result == -1:
            score = f"Advantage {self.player2_name}"
        elif minus_result >= 2:
            score = f"Win for {self.player1_name}"
        else:
            score = f"Win for {self.player2_name}"
        return score
    
    def _count_other_scores(self) -> str:
        score = ""
        for i in range(FIFTEEN, FORTY):
            if i == FIFTEEN:
                temp_score = self.m_score1
            else:
                score = score + "-"
                temp_score = self.m_score2

            score = score + SCORES[temp_score]
        return score

    def get_score(self):
        if self.m_score1 == self.m_score2:
            score = self._count_equal_scores()
        elif self.m_score1 >= GAME or self.m_score2 >= GAME:
            score = self._count_minus_scores()
        else:
            score = self._count_other_scores()

        return score
