"""This is my Pink Fluffy Unicorns quiz module"""
import colors as c
from utils import ask

intro = c.magenta + '''
Welcome to the Pnk Fluffy Unicorn quiz.
Lets test your knowledge...
'''

def q1():
    answer = ask("What color are the unicorns?"
    if answer == "pink":
        print("And what pretty color it is.")
        return True
    print("that is incorrect.")
    return False

def q2():
    answer = ask("What are the unicorns dancing on?")
    if answer .startwith("rainbow"):
        print("But isn't that physically impossible? Oh well.")
        return True
    print("Nope")
    return False

def q3():
    answer = ask("Use one word to describe their magical fur?")
    if answer .startwith("smile")
        print(":)")
        return True
    print(":<")
    return False

questions = [q1,q2,q3]

