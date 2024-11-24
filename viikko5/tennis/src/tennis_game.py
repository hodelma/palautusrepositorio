class TennisGame:

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.score_player1 = 0
        self.score_player2 = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.score_player1 += 1
        else:
            self.score_player2 += 1
    
    def tie(self):
        return self.score_player1 == self.score_player2

    def end_of_game(self):
        return self.score_player1 >= 4 or self.score_player2 >= 4
    
    def advantage_player(self):
        players_score_differences = self.score_player1 - self.score_player2
        if players_score_differences == 1:
            return f"Advantage {self.player1_name}"
        if players_score_differences == -1:
            return f"Advantage {self.player2_name}"
        if players_score_differences >= 2:
            return f"Win for {self.player1_name}"
        if players_score_differences <= -2:
            return f"Win for {self.player2_name}"
        
    def game_point_situation(self):
        player1_info = self.get_score_info(self.score_player1)
        player2_info = self.get_score_info(self.score_player2)
        return f"{player1_info}-{player2_info}"
        
    def get_score_info(self, score):
        if score == 0:
            return "Love"
        if score == 1:
            return "Fifteen"
        if score == 2:
            return "Thirty"
        if score == 3:
            return "Forty"
        
    def get_tie_score(self):
        if self.score_player1 == 0:
            return "Love-All"
        if self.score_player1 == 1:
            return "Fifteen-All"
        if self.score_player1 == 2:
            return "Thirty-All"
        else:
            return "Deuce"
    
    def get_score(self):
        if self.tie() == True:
            return self.get_tie_score()
        if self.end_of_game() == True:
            return self.advantage_player()
        else:
            return self.game_point_situation()
