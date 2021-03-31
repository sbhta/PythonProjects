import tkinter, sys
from config import *

window = tkinter.Tk()
window.geometry("600x540")
game_state = "not started"
cubes = []
for i in range(10): cubes.append(Cube(window, i))
for i in cubes:
    if cubes.index(i) == 1 or cubes.index(i) == 2 or cubes.index(i) == 3: i.pack_cubes()
for i in cubes:
    if cubes.index(i) == 4 or cubes.index(i) == 5 or cubes.index(i) == 6: i.pack_cubes()
for i in cubes:
    if cubes.index(i) == 7 or cubes.index(i) == 8 or cubes.index(i) == 9: i.pack_cubes()


def check_for_win():
    # checking for slides
    if cubes[1].state == cubes[2].state == cubes[3].state == ("X"): sys.exit()
    if cubes[4].state == cubes[5].state == cubes[6].state == ("X"): sys.exit()
    if cubes[7].state == cubes[8].state == cubes[9].state == ("X"): sys.exit()
    # checking for rows
    if cubes[1].state == cubes[4].state == cubes[7].state == ("X"): sys.exit()
    if cubes[2].state == cubes[5].state == cubes[8].state == ("X"): sys.exit()
    if cubes[3].state == cubes[6].state == cubes[9].state == ("X"): sys.exit()
    # in straights
    if cubes[1].state == cubes[5].state == cubes[9].state == ("X"): sys.exit()
    if cubes[3].state == cubes[5].state == cubes[7].state == ("X"): sys.exit()


while True:
    check_for_win()
    try:
        window.update()
    except:
        sys.exit()
