from karel.stanfordkarel import *
# writing a program to make Karel to pick the beeper and return back to its original position.


def main():
    while front_is_clear() and left_is_blocked():
        move()
        if front_is_blocked() and left_is_blocked():
            turn_right()
            move()
    else:
        turn_left()
        move()
        pick_beeper()
        turn_around()
    while front_is_clear():
        if front_is_clear():
            move()
    else:
        turn_right()
        move()
    turn_right()


"""   
def main():
    move()
    move()
    turn_right()
    move()
    turn_left()
    move()
    pick_beeper()
    turn_around()
    move()
    turn_right()
    move()
    turn_left()
    move()
    move()
    turn_around()
"""
# defining a helper function turn_right as Karel does't know how to move right
# and call it under main function


def turn_right():
    for i in range(3):
        turn_left()


def turn_around():
    for i in range(2):
        turn_left()

# There is no need to edit code beyond this point


if __name__ == "__main__":
    run_karel_program()