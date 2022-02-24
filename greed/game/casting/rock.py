from random import randint
from game.shared.color import Color
from game.shared.point import Point
from game.casting.actor import Actor

class Rock(Actor):
    # A falling object that takes away a point

    # Attributes for Rock:
    # _point_value(int): Point value of a rock.
    # set_text(method): Defines the charater representing a rock
    # set_color(method): Defines the color of a rock
    
  def __init__(self):
    super().__init__()
    self._point_value = -1
    self.set_text("o")
    self.set_color(Color(107,107,107)) 
    # (0,0,255) = the color blue
    sp = randint(2,3)                # falling spead of Rock 
    self.set_velocity(Point(0,2**sp))    # y by powers of 2

    self.set_velocity(Point(0,8)) # y by powers of 2?
    
    
  def get_point(self):
    #gets the point value of the rock
    return self._point_value



    