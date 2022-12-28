import os
from random import randint

from art import logo, vs
from game_data import data

# ______NOTES______
# game data is dict nested inside list so list[0] has 1 dict containing information retainning to that one person
# it might be easier to make a func called get_followers to get the info from game_data instead of typing out the path everytime
# your comparing followers
# b needs to be the next a
# need a checker func that checks if followers are > or < and then compares users guess with that takes 3 inputs and outputs "score + 1" or score
# need game_over = False bool inside game logic to act as the loop
# turns out i should probably make a get_bio() for generating the in game description of what your comparing....
# ______POST NOTES______
# I learned that even if you set the loop bool as false inside the loop it doesnt end the loop till after the loop is done
# to actually end it you have to make a if statement and have return like i do in game_logic()
# working with progressive variables that change with loops is hard remember to change ur previous score to the new score at the start of loop


def sclr():
    """clears terminal because python is stupid and doesnt have a built in func"""
    os.system("clear")


def get_data(ln, item="name"):
    """searches game data in list entry 'ln' for dict item 'item.' item needs quotes around it to function properly"""
    return data[ln][item]


def gen_bio(ln, n="name", fc="follower_count", d="description", c="country"):
    """(prints) generates a bio of person in 'ln' list entry"""
    print(f"{data[ln][n]} is a(n) {data[ln][d]} from (The) {data[ln][c]}.")


def checker(a_followers, b_followers, user_input, score):
    """compares a_followers to b_followers, saves as a var, and compares user input to it. if user input is right return 'score + 1'
    if its wrong return "score" to use in is_game_over to close the loop and end game"""
    if a_followers > b_followers and user_input == "a":
        return score + 1
    if b_followers > a_followers and user_input == "b":
        return score + 1
    else:
        return score


def is_game_over(new_score, score):
    """if current score is the same as high score game over return True"""
    if new_score == score:
        return True
    else:
        return False


def game_logic():
    """main game logic"""

    game_over = False
    score = 0
    new_score = 0
    a = randint(0, len(data) - 1)    # getting a list number to use for a
    a_followers = get_data(a, "follower_count")

    while game_over != True:
        sclr()
        b = randint(0, len(data) - 1)    # getting a list number to use for b
        b_followers = get_data(b, "follower_count")
        # if you dont have this line here your score stays at zero and new_score never goes past 1
        score = new_score

        while a == b:  # making sure b is a different value
            b = randint(1, len(data))

        print(logo)
        gen_bio(a)
        print(vs)
        gen_bio(b)
        print(f"Your current Score: {score}")
        user_input = input("Who do you think has the most followers? a/b\n")

        # easteregg
        if user_input != "a" and user_input != "b":
            print("BRO REALLY???? STOP MAKING ME CODE THESE ERROR CATCHES! screw u game over.... im done... dont relaunch my app!")
            return

        new_score = checker(a_followers, b_followers, user_input, score)
        if is_game_over(new_score, score):
            print("Too bad so sad you got that one wrong. GAME OVER.")
            print(f"Your final score was: {new_score}\n")
            return
        a = b
        a_followers = b_followers


sclr()
print(logo)
start = input("are ya ready kidzzzz??? y/n\n")
if start == "y":
    game_logic()
# easteregg
else:
    print("you think your slick huh? testing my code for simple errors.... well have fun this is the only error catch im coding in....")
