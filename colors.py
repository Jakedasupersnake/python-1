"""Hey this is my colors module.

My colors module is done.

"""

cyan ='\033[0;36m'
red = '\033[0;31m'
blue = '\033[0;34m'
yellow = '\033[0;33m'
green = '\033[0;32m'
violet = '\033[1;35m'
magenta = '\033[0;35m'
orange = '\033[1;31m'
base03 = '\033[1;30m'
base02 = '\033[0;30m'
base01 = '\033[1;32m'
base00 = '\033[1;33m'
base0 = '\033[1;34m'
base1 = '\033[1;36m'
base2 = '\033[0;37m'
base3 = '\033[1;37m' 
reset = '\033[0m'
clear = '\033[H\033[2J'
import random
def random_color():
    return random.choice([yellow, orange, red, magenta, violet, blue, cyan, green])

def clear_screen():
    print(clear)
if __name__ == '__main__':
    print(clear)
    print(red + 'red'+ reset)
    print(yellow + 'yellow'+ reset)
    print(magenta + 'magenta'+ reset)
    print(orange + 'orange'+ reset)
    print(cyan + 'cyan'+ reset)
    print(violet + 'violet')
    print(base3 + 'base3')
    print(base2 + 'base3')
    print(base1 + 'base1')
    print(base0 + 'base')
    print(base00 + 'base00')
    print(blue + 'blue')
    print(green + 'green')
    print(base01 + 'base01')
    print(base02 + 'base02')
    print(base03 + 'base03')

