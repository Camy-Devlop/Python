#importations
from tkinter import *
import webbrowser
import tkinter as tk
from PIL import Image, ImageTk
import te
#definition de fonctions

def cours_du_navets ():
    webbrowser.open_new("https://turnipprophet.io/index.html")

def new_horizons_inventory ():
    webbrowser.open_new("https://newhorizonsinventory.com/")

def ac_patterns_online ():
    webbrowser.open_new("https://acpatterns.com/")


def second_window():
    window2 = Toplevel(bg='white')
    window2.title("Votre Île")
    #window2.iconbitmap("Logo_Acnh.ico")



# créer une première fenetre
window = Tk()





# personnaliser cette fenêtre
window.title("Animal Crossing New Horizons")
window.geometry("1020x600")
#window.iconbitmap("Logo_Acnh.ico")
window.config(background='#0DA218')

# créer une boite pour la fenetre pop-up
frame = Frame(bg= '#0DA218')
frame.grid(row = 5, column = 1)

#créer une deuxieme boite avec le champ entréer
frame2 = Frame(window, bg= '#0DA218')
frame2.grid(row = 3, column = 1)

# créer la boite
frame = Frame(window, bg= '#0DA218')
frame.grid(row = 5, column = 1)


# ajouter un premier texte
label_title = Label(frame, text="Bienvenue sur l'Application", font = ("Comic Sans", 40), bg='#0DA218', fg = 'white')
label_title.grid(row = 5, column = 1)

# ajouter un second texte
label_subtitle = Label(frame, text="By Siuol2k05", font = ("Comic Sans MS", 25), bg='#0DA218', fg = 'white')
label_subtitle.grid(row = 7, column = 1 )

# ajouter un bouton cours du navet
cours_du_navets = Button(window, text="Cours du Navet", font = ("Comic Sans", 25), bg='#0DA218', fg ='white', command= cours_du_navets)
cours_du_navets.grid(row = 3, column = 2, sticky = 'ns', pady = 2)


# ajouter un bouton new horizons inventory
new_horizons_inventory = Button(window, text="New Horizons Inventory", font = ("Comic Sans", 25), bg='#0DA218', fg ='white', command= new_horizons_inventory)
new_horizons_inventory.grid(row = 4, column = 2, sticky = 'ns', pady = 20)


# ajouter un boutton de validation
validate_button = Button(window, text="Valider", font = ("Comic Sans", 25), bg='#0DA218', fg ='white', command = second_window)
validate_button.grid(row = 5, column = 1, sticky = 'ns', pady = 20)

# création d'image CELESTE
width = 150
height = 180
animation = Image.open("tenor.gif")
#animation.show()
image = PhotoImage(file="tenor.gif")
canvas = Canvas(window, width=width, height=height, bg='#0DA218', highlightthickness = 0)
canvas.create_image(width/2, height/2, image=image)
canvas.grid(row = 1,column =0, sticky = 'ns', rowspan = 2)




#création d'une barre de menu
menu_barre = Menu(window)

#créer un premier menu
file_menu = Menu(menu_barre)
file_menu.add_command(label="Quitter", command=window.quit)
menu_barre.add_cascade(label="Informations", menu=file_menu)
file_menu.add_cascade(label="Version : Alpha 0.0.1 ")


#configurer notre fenetre pour ajouter cette menue bar
window.config(menu=menu_barre)

#ajout d'un champ enter
nom_ile = tk.StringVar(window)
nom_ile.set("Nom de votre Île")
name_island = Entry(window, font = ("Comic Sans MS", 20), fg = 'black', textvariable = nom_ile)
name_island.grid(row = 3, column = 1)


#ajout d'un second champ enter
fruit = tk.StringVar(window)
fruit.set("Votre fruit de départ")
fruit_island = Entry(window, font = ("Comic Sans MS", 20), fg = 'black', textvariable = fruit)
fruit_island.grid(row = 4, column = 1)

#ajout d'un premier champ enter pour la fenetre pop-up
affichage_fruit_island = Entry(frame2, font = ("Comic Sans MS", 20), fg = 'black', textvariable = fruit)
affichage_fruit_island.grid(row = 1, column = 1)


# ajouter la boite
frame.grid(row = 1,column = 1, sticky = 'ns', rowspan = 2)


# afficher la fenetre




window.mainloop()