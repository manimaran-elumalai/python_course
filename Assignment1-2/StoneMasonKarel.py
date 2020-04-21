from karel.stanfordkarel import *

"""
Pre Condition: Check if Karel is facing east
Pre Condition: Replace the missing stones from the arches with beepers
"""


def main():
    if front_is_clear() and left_is_clear() and right_is_blocked():
        for i in range(3):
            repair_arches()
        turn_left()
        turn_move_north()
        turn_around()
        turn_move_south()


"""
Pre Condition: Turn left and move facing North and replace the missing stone from arches with beepers
Post Condition: Turn around and move facing south and replace the missing stone from the arches with beepers and
move to next arches.
"""


def repair_arches():
    turn_left()
    turn_move_north()
    turn_around()
    turn_move_south()
    move_to_next_corner()


"""
Pre Condition: Move facing north
Post Condition: Replace the missing stone with beepers
"""


def turn_move_north():
    while front_is_clear():
        if beepers_present():
            move()
        else:
            put_beeper()
    if no_beepers_present():
        put_beeper()


"""
Pre Condition: Check if front is clear
Post Condition: Karel moves to the end facing south and turns east
"""


def turn_move_south():
    while front_is_clear():
        move()
    turn_left()


"""
Pre Condition: Check if front clear facing east
Post Condition: Move to next arch
"""


def move_to_next_corner():
    for i in range(4):
        move()


def turn_around():
    turn_left()
    turn_left()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
