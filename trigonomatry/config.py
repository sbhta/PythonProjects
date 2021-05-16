import math
from math import cos, tan, sin, atan,radians, sqrt, degrees

inp = input("if you have 2 edges and 1 angle type 1, if you have 1 edge and to angles type 2: ")

while True:
    if inp == ("1" or "2"): break
    inp = input("please type one of the options(1, 2): ")

if inp == "1":
    def f1(a, b):
        c_powered = a ** 2 + b ** 2
        return int(math.sqrt(c_powered))


    def f2(b, c):
        a_powered = b ** 2 + c ** 2 - 2 * b * c(cos(radians(float(angle))))
        return sqrt(a_powered)


    angle = float(input("the theta: "))
    a = int(input("the opp: "))
    b = int(input("the adj: "))

    print(f"""
the opp of theta is {a}
the adj of theta is {b}
the hyp of theta is {f1(int(a), int(b))}

the theta of opp and adj is {degrees(atan(radians(a)/radians(b)))}""")




elif inp == "2":
    edge = input()
    angle1 = input()
    angle2 = input()
