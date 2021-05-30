import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

screen = [
    ["g","g","g","g","g","g","g","g","g","g","g","g"],
    ["g","g","g","g","g","g","g","g","g","g","g","g"],
    ["g","g","g","g","g","g","g","g","g","g","g","g"],
    ["g","g","g","g","g","g","g","g","g","g","g","g"],
    ["g","g","g","g","g","\x1b[31m@","g","g","g","g","g","g"],
    ["g","g","g","g","g","g","g","g","g","g","g","g"],
    ["g","g","g","g","g","g","g","g","g","g","g","g"],
    ["g","g","g","g","g","g","g","g","g","g","g","g"],
    ["g","g","g","g","g","g","g","g","g","g","g","g"],
    ["g","g","g","g","g","g","g","g","g","g","g","g"],

]

#print("\e[0;32mclass")
def print_field():
    for i in screen:
        print(end="""
""")
        for j in i:
            print(j, end=" ")
    print("""
""")

def clamp(n, smallest, largest):
    return max(smallest, min(n, largest))
while True:
    print_field()
    inp = input("Next: ")
    if inp == "d":
        for i in range(len(screen)):
            if Fore.RED + "@" in screen[i]:
                try: a, b = screen[i].index(Fore.RED + "@"), screen[i].index(Fore.RED + "@") + 1; screen[i][b], screen[i][a] = screen[i][a], screen[i][b]; break
                except: pass
    elif inp == "a":
        for i in range(len(screen)):
            if Fore.RED + "@" in screen[i]:
                try: a, b = screen[i].index(Fore.RED + "@"), screen[i].index(Fore.RED + "@") - 1; screen[i][b], screen[i][a] = screen[i][a], screen[i][b]; break
                except: pass
    elif inp == "s":
        for i in range(len(screen)):
            if Fore.RED + "@" in screen[i]:
                try: a, b = screen[i].index(Fore.RED + "@"), screen[i].index(Fore.RED + "@"); screen[i+1][b], screen[i][a] = screen[i][a], screen[i+1][b]; break
                except: pass
    elif inp == "w":
        for i in range(len(screen)):
            if Fore.RED + "@" in screen[i]:
                try: a, b = screen[i].index(Fore.RED + "@"), screen[i].index(Fore.RED + "@"); screen[i-1][b], screen[i][a] = screen[i][a], screen[i-1][b]; break
                except: pass


        