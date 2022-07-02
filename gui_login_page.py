from tkinter import *
import os
import tkinter as tk 

def registracija():
    global vartotojo_registracija
    vartotojo_registracija = Toplevel(platforma)
    vartotojo_registracija.geometry("400x200")
    vartotojo_registracija.iconbitmap('Stocks_31093.ico')
    vartotojo_registracija.title('Popierių info')

    global vardas
    global slaptazodis
    global vardo_ivedimas
    global slapt_ivedimas
    vardas = StringVar()
    slaptazodis = StringVar()

    Label(vartotojo_registracija, text="Įveskite savo duomenis:").pack()
    Label(vartotojo_registracija, text="").pack()
    vardo_antraste = Label(vartotojo_registracija, text="Vartotojo vardas:")
    vardo_antraste.pack()
    vardo_ivedimas = Entry(vartotojo_registracija, textvariable=vardas)
    vardo_ivedimas.pack()
    slapt_antraste = Label(vartotojo_registracija, text="Slaptažodis:")
    slapt_antraste.pack()
    slapt_ivedimas = Entry(vartotojo_registracija, textvariable=slaptazodis, show='*')
    slapt_ivedimas.pack()
    Label(vartotojo_registracija, text="").pack()
    Button(vartotojo_registracija, text="REGISTRUOTIS", width=15, height=1, bg="pink", activebackground="red", command = uzregistruoti).pack()

def uzregistruoti():
    vardo_info = vardas.get()
    slapt_info = slaptazodis.get()
    file = open(vardo_info, "w+")
    file.write(vardo_info + "\n")
    file.write(slapt_info)
    file.close()
    vardo_ivedimas.delete(0, END)
    slapt_ivedimas.delete(0, END)
    Label(vartotojo_registracija, text="Registracija sėkminga!", fg="green", font=("calibri", 13)).pack()

def prisijungimas():
    global vartotojo_login
    vartotojo_login = Toplevel(platforma)
    vartotojo_login.geometry("400x200")
    vartotojo_login.iconbitmap('Stocks_31093.ico')
    vartotojo_login.title('Popierių info')
    Label(vartotojo_login, text="Įveskite savo duomenis:").pack()
    Label(vartotojo_login, text="").pack()
    global slapta_pat
    global vardas_pat
    vardas_pat = StringVar()
    slapta_pat = StringVar()
    global vardo_ivedimas2
    global slapt_ivedimas2
    Label(vartotojo_login, text="Vartotojo vardas")
    vardo_ivedimas2 = Entry(vartotojo_login, textvariable=vardas_pat)
    vardo_ivedimas2.pack()
    Label(vartotojo_login, text="").pack()
    Label(vartotojo_login, text="Slaptažodis")
    slapt_ivedimas2 = Entry(vartotojo_login, textvariable=slapta_pat, show='*')
    slapt_ivedimas2.pack()
    Label(vartotojo_login, text="").pack()
    Button(vartotojo_login, text="PRISIJUNGTI", width=15, height=1, bg="pink", activebackground="red", command= prisijungimo_patviritnimas).pack()

def prisijungimo_patviritnimas():
    vardas1 = vardas_pat.get()
    slapta1 = slapta_pat.get()
    vardo_ivedimas2.delete(0, END)
    slapt_ivedimas2.delete(0, END)
 
    list_of_files = os.listdir()
    if vardas1 in list_of_files:
        file1 = open(vardas1, "r")
        verify = file1.read().splitlines()
        if slapta1 in verify:
            pavyko()
            
        else:
            Label(vartotojo_login, text="Blogas slaptažodis!", fg="red", font=("calibri", 11)).pack()
 
    else:
        Label(vartotojo_login, text="Vartotojo paskyra neegzistuoja!", fg="red", font=("calibri", 11)).pack()

def pavyko():

    import paper as p
    os.system(paper)
    paper = 'paper.py'

def platformos_langas():
    global platforma
    platforma = Tk()
    platforma.geometry("400x200")
    platforma.iconbitmap('Stocks_31093.ico')
    platforma.title('Popierių info')
    Label(text="").pack()
    Button(text="Login", height="1", width="25", command = prisijungimas).pack()
    Label(text="").pack()
    Button(text="Register", height="1", width="25", command = registracija, ).pack()
    platforma.mainloop()

platformos_langas()
