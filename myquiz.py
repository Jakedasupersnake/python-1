"""this is my quiz module"""

import colors as c
from utils import ask

intro = c.magenta + '''
Welcome to my quiz.
I hope you do good.
'''

def q1():
    answer = ask("What wool color does white wool and pink dye make?")
    if answer == "pink":
        print("Good job")
        return True
    print("that is incorrect.")
    return False

def q2():
    answer = ask("How many letters on a keyboard?")
    if answer == "26":
        print("Super.")
        return True
    print("Nope")
    return False

def q3():
    answer = ask("What number is this:1000000?")
    if answer == "1 million":
        print(":)")
        return True
    print(":<")
    return False

questions = [q1,q2,q3]
