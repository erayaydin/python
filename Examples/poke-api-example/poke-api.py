 public_htmlimport json
import requests

apiUrl = "http://pokeapi.co/api/v2/"

sonrakiSayfa = apiUrl+"pokemon/"

while(sonrakiSayfa != None):
  pokemonListesi = requests.get(sonrakiSayfa)
  pokemonListesi = pokemonListesi.content.decode('utf-8')
  pokemonlar = json.loads(pokemonListesi)

  for pokemon in pokemonlar['results']:
    pokemonDetay = requests.get(pokemon['url'])
    pokemonDetay = pokemonDetay.content.decode('utf-8')
    pokemon = json.loads(pokemonDetay)
    print(pokemon['name']+" --> "+str(pokemon['weight']))

  sonrakiSayfa = pokemonlar['next']
