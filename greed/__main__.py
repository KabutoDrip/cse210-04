import random

from game.casting.cast import Cast
from game.casting.actor import Actor
from game.casting.gem import Gem
from game.casting.rock import Rock
from game.casting.player import Player


from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point


FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 24
FONT_SIZE = 24
COLS = MAX_X // CELL_SIZE
ROWS = MAX_Y // CELL_SIZE
CAPTION = "Greed"
WHITE = Color(255, 255, 255)
FALLING_GEMS = 20
FALLING_ROCKS = 20


def main():
    # create the cast
    cast = Cast()
    
    # create the banner
    banner = Actor()
    banner.set_text("")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)
    
    # create the player
    x = int(COLS // 2)
    y = ROWS -2
    position = Point(x, y)
    position = position.scale(CELL_SIZE)               

    

    player = Player()
    player.set_text("_")
    player.set_font_size(FONT_SIZE)
    player.set_color(WHITE)
    player.set_position(position)
    cast.add_actor("player", player)
    
    
    # creates the falling objects and adds them to the cast
   
    for n in range(FALLING_GEMS):
        x = random.randint(1, COLS - 2)
        y = random.randint(1, ROWS - 2)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)               
        gem = Gem()
        gem.set_position(position)
        cast.add_actor("falling_objects", gem)

    for n in range(FALLING_ROCKS):
        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)               
        rock = Rock()
        rock.set_position(position)
        cast.add_actor("falling_objects", rock)    
    
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()