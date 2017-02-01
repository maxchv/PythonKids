import io
import json
import urllib.request
from urllib.request import urlopen, Request
from PIL import Image, ImageTk
from shutil import copyfileobj
import shelve

#function to get the data for a pokemon
def getPokemonData(num):
    req = Request("http://pokeapi.co/api/v1/pokemon/"+str(num))
    req.add_header('User-agent', 'Mozilla/5.0')
    data = urlopen(req).read()
    pokemonDict = json.loads(data.decode("UTF-8"))
    return pokemonDict

def getPokemonData2(num):
    pokemonDict = None
    with shelve.open('pokemons') as d:
        #print("open shelve")
        #print(d['pokemons'])
        if num >=0 and num < len(d['pokemons']):
            pokemonDict = d['pokemons'][num]
    return pokemonDict

#function to get the image for a pokemon
def getPokemonImage(num):
    req = Request("http://pokeapi.co/api/v1/sprite/"+str(num))
    req.add_header('User-agent', 'Mozilla/5.0')
    data = urlopen(req).read()
    spriteDict = json.loads(data.decode("UTF-8"))
    imgURL = "http://pokeapi.co" + spriteDict["image"]
    req = Request(imgURL)
    req.add_header('User-agent', 'Mozilla/5.0')
    image_bytes = urlopen(req).read()
    data_stream = io.BytesIO(image_bytes)
    pil_image = Image.open(data_stream)
    tk_image = ImageTk.PhotoImage(pil_image)
    return tk_image

def getPokemonImage2(pokemonDict):
    tk_image = None
    with open(pokemonDict['image'], 'rb') as image_bytes:
        #data_stream = io.BytesIO(image_bytes)
        pil_image = Image.open(image_bytes)
        tk_image = ImageTk.PhotoImage(pil_image)
    return tk_image

def downloadPokemonImage(num):
    req = Request("http://pokeapi.co/api/v1/sprite/"+str(num))
    req.add_header('User-agent', 'Mozilla/5.0')
    data = urlopen(req).read()
    spriteDict = json.loads(data.decode("UTF-8"))
    imgURL = "http://pokeapi.co" + spriteDict["image"]
    out_img = "sprites\\"+ spriteDict["name"] + ".png"
    req = Request(imgURL)
    req.add_header('User-agent', 'Mozilla/5.0')
    with urlopen(req) as in_stream, open(out_img, 'wb') as out_stream:
        copyfileobj(in_stream, out_stream)
    return out_img
