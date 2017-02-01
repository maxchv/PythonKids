from random import *
import tkinter
import urllib.request
from urllib.request import urlopen
from PIL import Image, ImageTk
import io
from pokemontcgsdk import Card

smallFont = ["Ariel" , 10]
mediumFont = ["Ariel" , 14]
bigFont = ["Ariel" , 24]

def pokemonImage(imgURL):
    image_bytes = urlopen(imgURL).read()
    data_stream = io.BytesIO(image_bytes)
    pil_image = Image.open(data_stream)
    tk_image = ImageTk.PhotoImage(pil_image)
    return tk_image

#function to display data for a pokemon number
def showPokemonData():
    #get the number typed into the entry box
    pokemonNumber = randint(0, 99)

    #use the function above to get the pokemon data
    pokemon = Card.where(page=1).array()[pokemonNumber]

    #get the data from the dictionary and add it to the labels
    lblNameValue.configure(text = pokemon.get('name'))
    lblHPValue.configure(text = pokemon.get('hp'))
    lblAttackValue.configure(text = pokemon.get('attacks')[0]['damage'] if pokemon.get('attacks') else '?')
    lblDefenceValue.configure(text = pokemon.get("resistances")[0]['type'] if pokemon.get("resistances") else '?')
    #lblSpeedValue.configure(text = pokemonDictionary["speed"])
    
    #add the image and add it to a label
    img = pokemonImage(pokemon.get('imageUrl'))
    lblImage.configure(image=img)
    lblImage.image = img

#create the main window
window = tkinter.Tk()
window.config(bg="#e0e0ff")
window.title("Pokedex")

#button to show a random pokemon
btnGo = tkinter.Button(window,text="Get Random Pokemon!",
                       command=showPokemonData, font=smallFont)
btnGo.pack()

#pokemon name
lblNameText = tkinter.Label(window,text="Name:", font=mediumFont)
lblNameText.config(bg="#e0e0ff", fg="#111111")
lblNameText.pack()
lblNameValue = tkinter.Label(window,text="?", font=bigFont)
lblNameValue.config(bg="#e0e0ff", fg="#111111")
lblNameValue.pack()

#pokemon hp
lblHPText = tkinter.Label(window,text="HP:", font=mediumFont)
lblHPText.config(bg="#e0e0ff", fg="#111111")
lblHPText.pack()
lblHPValue = tkinter.Label(window,text="?", font=bigFont)
lblHPValue.config(bg="#e0e0ff", fg="#111111")
lblHPValue.pack()

#pokemon attack
lblAttackText = tkinter.Label(window,text="Attack:", font=mediumFont)
lblAttackText.config(bg="#e0e0ff", fg="#111111")
lblAttackText.pack()
lblAttackValue = tkinter.Label(window,text="?", font=bigFont)
lblAttackValue.config(bg="#e0e0ff", fg="#111111")
lblAttackValue.pack()

#pokemon defence
lblDefenceText = tkinter.Label(window,text="Defence:", font=mediumFont)
lblDefenceText.config(bg="#e0e0ff", fg="#111111")
lblDefenceText.pack()
lblDefenceValue = tkinter.Label(window,text="?", font=bigFont)
lblDefenceValue.config(bg="#e0e0ff", fg="#111111")
lblDefenceValue.pack()

#pokemon speed
lblSpeedText = tkinter.Label(window,text="Speed:", font=mediumFont)
lblSpeedText.config(bg="#e0e0ff", fg="#111111")
lblSpeedText.pack()
lblSpeedValue = tkinter.Label(window,text="?", font=bigFont)
lblSpeedValue.config(bg="#e0e0ff", fg="#111111")
lblSpeedValue.pack()

#labal for the pokemon image
lblImage = tkinter.Label(window)
lblImage.config(bg="#e0e0ff", fg="#111111")
lblImage.pack()

window.mainloop()

    
