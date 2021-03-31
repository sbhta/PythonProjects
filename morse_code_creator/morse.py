from winsound import Beep
from time import sleep

short = lambda: "."
long = lambda: "_"

alpha = {
    "a": [short(), long()],
    "b": [long(), short(), short(), short()],
    "c": [long(), short(), long(), short()],
    "d": [long(), short(), short()],
    "e": [short()],
    "f": [short(), short(), long(), short()],
    "g": [long(), long(), short()],
    "h": [short(), short(), short(), short()],
    "i": [short(), short()],
    "j": [short(), long(), long(), long()],
    "k": [long(), short(), long()],
    "l": [short(), long(), short(), short()],
    "m": [long(), long()],
    "n": [long(), short()],
    "o": [long(), long(), long()],
    "p": [short(), long(), long(), short()],
    "q": [long(), long(), short(), long()],
    "r": [short(), long(), short()],
    "s": [short(), short(), short()],
    "t": [long()],
    "u": [short(), short(), long()],
    "v": [short(), short(), short(), long()],
    "w": [short(), long(), long()],
    "x": [long(), short(), short(), long()],
    "y": [long(), short(), long(), long()],
    "z": [long(), long(), short(), short()],
    " ": [" "]
}


def trans(string):
    newArray = []
    for i in string: newArray.append(alpha.get(i))
    print(newArray)

    for i in newArray:
        for j in i:
            if j == ".": Beep(440, 200)
            if j == "_": Beep(440, 600)
            else: sleep(0.25)
        sleep(0.25)


trans("daniel")
