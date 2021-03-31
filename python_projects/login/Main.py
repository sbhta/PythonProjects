from Classes import *
import os
import hashlib



hashing = lambda string:hashlib.sha256(str.encode(string)).hexdigest()


print(__file__.replace("Main.py", ""))

if __name__ == "__main__":
    reg = str(input("Register? (y/n)").lower())
    if reg == "y":
        def register():
            try:
                new_user = User(str(input("username: ")).replace(" ", ""), input(("password: ")).replace(" ", ""))
                path = __file__.replace("Main.py", "") + "users/{}'s_file".format(new_user.username)
                os.mkdir(path)
                file = open("users/{}'s_file/{}.txt".format(new_user.username, new_user.username), "w")
                file.write("{}'s account:".format(new_user.username))
                file.write("\n{}".format(new_user.username))
                file.write("\n{}".format(hashing(new_user.password)))
                print("Hello and welcome {}".format(new_user.username))
            except FileExistsError:
                print("Username already in use please try another username")
                register()


        register()
    elif reg == "n":
        def ask():
            username = input("username: ")
            password = input("password: ").replace(" ", "")
            try:
                file = open("users/{}'s_file/{}.txt".format(username, username), "r")
                if file.readlines()[2] == hashing(password):
                    print("hello {}".format(username))
                    file.close()
                else:
                    print("wrong password or username")
                    print("try again\n")
                    ask()
            except FileNotFoundError:
                print("wrong password or username")
                print("try again\n")
                ask()


        ask()
    else:
        print("invalid input")
