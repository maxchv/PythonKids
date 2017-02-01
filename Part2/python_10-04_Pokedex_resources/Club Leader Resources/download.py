import shelve
from pokeapi import getPokemonData, downloadPokemonImage
d = shelve.open('pokemons')
d['pokemons'] = []
for i in range(1, 200):
    p = getPokemonData(i)
    p['image'] = downloadPokemonImage(i)
    d['pokemons']+=[p]
    print(i, end=', ')
d.close()
