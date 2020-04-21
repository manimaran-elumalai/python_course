from karel.stanfordkarel import *


"""
Pre Condition: Karel starting position is facing west from the upper right corner of the left building
Post Condition: Karel paints all the 3 building, ends facing west on the left corner of the right building 
without placing beeper
"""


def main():
    move_west()
    turn_left()
    move()
    move_south_east()
    turn_right()
    move_south_east()
    turn_left()
    move()
    move_north()
    turn_right()
    move_east()
    turn_left()
    move()
    move_north()
    turn_left()
    move()
    move_west()


def move_south_east():
    move_south()
    turn_left()
    move()
    move_east()


def move_west():
    while front_is_clear() and left_is_blocked():
        put_beeper()
        move()


def move_south():
    while front_is_clear() and left_is_blocked():
        put_beeper()
        move()


def move_east():
    while front_is_clear() and left_is_blocked():
        put_beeper()
        move()


def move_north():
    while front_is_clear() and left_is_blocked():
        put_beeper()
        move()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


# There is no need to edit code beyond this point


if __name__ == "__main__":
    run_karel_program()
