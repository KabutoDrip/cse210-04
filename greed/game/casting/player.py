from game.casting.actor import Actor
from game.casting.cast import Cast    
from game.casting.rock import Rock
from game.casting.gem import Gem
class Player(Actor):

    def __init__(self):
        super().__init__()
        self._message = ""
        self._score = 0
        
    def get_score(self):
        # gets the current score of the game
        return self._score
    def update_score(self):
        # updates the score of the 
        score_mod = object.get_point()
        self._score += score_mod
        return self._score
    def give_score(self,score):
        self._score = score
        return self._score