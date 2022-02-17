from game.casting.actor import Actor

class Artifact(Actor):
    # responsibility of this class is to return info based on what item is collected
    def __init__(self):
        super().__init__()
        self._collected = ""
    def get_collected(self):
    #gets the collected items type
        return self._collected
    def update_score(self, collected):
        self._collected = collected
    # updates score based on collected item
    
    