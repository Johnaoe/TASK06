import random
import tkinter as tk
from tkinter import *

paper = Tk()
paper.geometry("400x200")
paper.iconbitmap('Stocks_31093.ico')
paper.title('Popierių info')

PLAYER_REZ = 0
RNG_REZ = 0
PLAYER_PICK = ""
RNG_PICK = ""

def randomly_generated_numbers():
        return random.choice(['popierius','akmuo','žirklės'])
    
def reiksmes(choice):
        keit={'popierius':0, 'akmuo':1, 'žirklės':2}
        return keit[choice]
    
def rng_reiksmes(number):
        keit={0:'popierius', 1:'akmuo', 2:'žirklės'}
        return keit[number]
    
def result(player_picks, rng_picks):
        global PLAYER_REZ
        global RNG_REZ

        player = reiksmes(player_picks)
        rng = reiksmes(rng_picks)

        if(player==rng):
                print("Lygiosios")
        elif((player-rng)%3==1):
                print("Pralaimėjai")
                PLAYER_REZ+=1
        else:
                print("Laimėjai!")
                RNG_REZ+=1

        informacija = tk.Text(master=paper, height=4, width=40)
        informacija.pack()
        rezultatai = "Tavo pasirinkimas: {a}\nPriešininko pasirinkimas: {b}\nTavo rez.: {c}\nPriešininko rez.: {d}".format(a=PLAYER_PICK, b=RNG_PICK, c=PLAYER_REZ, d=RNG_REZ)
        informacija.insert(tk.END, rezultatai)

def akmuo():
        global PLAYER_PICK
        global RNG_PICK
        PLAYER_PICK='akmuo'
        RNG_PICK=randomly_generated_numbers()
        result(PLAYER_PICK, RNG_PICK)

def popierius():
        global PLAYER_PICK
        global RNG_PICK
        PLAYER_PICK='popierius'
        RNG_PICK=randomly_generated_numbers()
        result(PLAYER_PICK, RNG_PICK)

def žirklės():
        global PLAYER_PICK
        global RNG_PICK
        PLAYER_PICK='žirklės'
        RNG_PICK=randomly_generated_numbers()
        result(PLAYER_PICK, RNG_PICK)

Label(text="").pack()
Button(text="popierius", height="2", width="25", command = popierius, bg="goldenrod", master=paper).pack()
Label(text="").pack()
Button(text="žirklės", height="2", width="25", command = žirklės, bg="aquamarine", master=paper).pack()
Label(text="").pack()
Button(text="akmuo", height="2", width="25", command = akmuo, bg="bisque", master=paper).pack()

paper.mainloop()