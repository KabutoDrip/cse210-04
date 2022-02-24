from game.casting.actor import Actor
    
class Player(Actor):

    def __init__(self):
        super().__init__()
        self._message = ""
        self._score = 0
        
    def get_score(self):
        ##gets the current score of the game
        return self._score
    def update_score(self, score):
        ##updates the score of the 
        ()
    def give_score(self):
        ()