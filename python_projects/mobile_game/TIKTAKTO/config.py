import tkinter
player_state="X"
game_state = False
class Cube:
    def __init__(self, window, num):
        self.state = 0
        self.button = tkinter.Button(window,command=self.button_command, font=("ariel", 40), padx=80, pady=40)
        self.num = num
    def button_command(self):
        global player_state
        self.button.config(state="disabled")
        self.button.config(text=player_state)
        self.state = player_state
        if player_state == "X": player_state = "O"; self.button.config(padx=62)
        elif player_state == "O": player_state = "X"; self.button.config(padx=59)
    def change_state(self, state):
        self.button.config(text=state, font=(40))
    def pack_cubes(self):
        if self.num == 1:  self.button.place(x=0, y=0)
        if self.num == 2:  self.button.place(x=205, y=0)
        if self.num == 3:  self.button.place(x=410, y=0)
        if self.num == 4:  self.button.place(x=0, y=183)
        if self.num == 5:  self.button.place(x=205, y=183)
        if self.num == 6:  self.button.place(x=410, y=183)
        if self.num == 7:  self.button.place(x=0, y=366)
        if self.num == 8:  self.button.place(x=205, y=366)
        if self.num == 9:  self.button.place(x=410, y=366)


