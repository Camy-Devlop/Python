
#! /usr/local/bin/python3
from tkinter import *

from Pkg.Batiments.Immeuble import Immeuble
from Pkg.Batiments.Appartement import Appartement 

class main(object):
  
    print("bienvenu dans ma ville")
    window =Tk()
    label = Label(fenetre, text="Hello World")
    label.pack()

    window.mainloop()