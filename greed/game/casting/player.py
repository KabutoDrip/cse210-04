from game.casting.actor import Actor
from game.casting.cast import Cast    
from game.casting.rock import Rock
from game.casting.gem import Gem
from game.directing.director import Director
class Player(Actor):

    def __init__(self):
        super().__init__()
        self._score = 1
        
    def get_score(self):
        # gets the current score of the game
        return self._score
    def update_score(self, object_value):
        # updates the score of the 
        self._score += object_value
        return self._score
   