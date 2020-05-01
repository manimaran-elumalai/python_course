"""
File: nimm.py
-------------------------
Add your comments here.
"""


def main():
    stones = 20
    print("There are " + str(stones) + " stones left")
    switch = True
    while stones > 0:
        player = fetch_user_input(stones)
        stones -= player
        if stones <= 0:
            print("] Wins")
        # ME: handle if stones is zero, what to do?
        print("Main: There are " + str(stones) + " stones left")
        player2 = fetch_user_input(stones)
        stones -= player2
        if stones <= 0:
            print("Player1 Wins")
    # ME: handle if stones is zero, what to do?
        print("Main: There are " + str(stones) + " stones left")
    print("Game over!")
    return


"""‹
# Write a function named fetch_input
# Function should return 1/2 after accepting input from user
# if user enters more than two show him error accept new input
# Replace the input in line 12 and 16 with fetch_input function
"""


def fetch_user_input(left_over_stones):
    num = int(input("fetch_user_input : remove 1 or 2 stones? "))
    while num > left_over_stones or num > 2 or num <= 0:
        print("Please enter 1 or 2")
        num = int(input("fetch_user_input : remove 1 or 2 stones? "))
    return num


"""
    You should write your code for this program in this function.
    Make sure to delete the 'pass' line before starting to write
    your own code. You should also delete this comment and replace
    it with a better, more descriptive one.
"""


def player_turn():
    print("There are 20 stones left")
    player1 = int(input("Player 1 would you like to remove 1 or 2 stones? "))
    player2 = int(input("Player 2 would you like to remove 1 or 2 stones? "))


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
