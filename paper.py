import random
import tkinter as tk

paper=tk.Tk()
paper.geometry("300x400")

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

        informacija = tk.Text(master=paper, height=12, width=40)
        informacija.grid(column=15, row=4)
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

b1=tk.Button(text="Žirklės", bg="goldenrod",command=žirklės, height=1, width=40, font=('calibri', 12))
b1.grid(column=15, row=1)
b2=tk.Button(text="Popierius", bg="aquamarine", command=popierius, height=1, width=40, font=('calibri', 12))
b2.grid(column=15, row=2)
b3=tk.Button(text="Akmuo", bg="bisque",command=akmuo, height=1,width=40, font=('calibri', 12))
b3.grid(column=15, row=3)  

paper.mainloop()