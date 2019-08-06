# Gerekli paketlerin yüklenmesi
import requests
import json

# Pokemon sınıfı...
class Pokemon:
  
  def __init__(self, adi, agirlik=0, boy=0, yetenekler=[], hiz=0, savunma=0, saldiri=0, can=0, resim=None):
    self.adi = adi
    self.agirlik = agirlik
    self.boy = boy
    self.yetenekler = yetenekler
    self.hiz = hiz
    self.savunma = savunma
    self.saldiri = saldiri
    self.can = can
    self.resim = resim

  def hasarVer(self, pokemon):
    if self.can > 0:
      pokemon.hasarAl(self)
    else:
      print(self.adi+" pokemonunun saldırmak için canı yok")

  def hasarAl(self, pokemon):
    if self.can > 0:
      self.can -= pokemon.saldiri
    else:
      print(self.adi+" pokemonu zaten ölü")

  def yetenekKullan(self, isim):
  	print(self.adi+" "+isim+" yeteneğini kullanıyor.")

# Pokemon bilgilerinin çekilmesi...
pokemonlar = {}
apiUrl = "http://pokeapi.co/api/v2/"

pokemonListesi = requests.get(apiUrl+"pokemon/") # http://pokeapi.co/api/v2/pokemon/
pokemonListesi = pokemonListesi.content.decode("utf-8")
pokemonlarJSON = json.loads(pokemonListesi)

i = 1
for pokemonMeta in pokemonlarJSON['results']:
	pokemonDetayString = requests.get(pokemonMeta['url'])
	pokemonDetayString = pokemonDetayString.content.decode('utf-8')
	pd = json.loads(pokemonDetayString)

	yetenekler = []

	for yetenek in pd['abilities']:
		if yetenek["ability"] != None and yetenek["ability"]["name"] != None:
		  yetenekler.append(yetenek["ability"]["name"])

	pokemonNesnesi = Pokemon(
		pd['name'],
		pd['weight'],
		pd['height'],
		yetenekler
	)

	for biri in pd['stats']:
		statName = biri['stat']['name']

		if statName == "speed":
			pokemonNesnesi.hiz = biri['base_stat']
		elif statName == "defense":
			pokemonNesnesi.savunma = biri['base_stat']
		elif statName == "attack":
			pokemonNesnesi.saldiri = biri['base_stat']
		elif statName == "hp":
			pokemonNesnesi.can = biri['base_stat']

	pokemonNesnesi.resim = pd["sprites"]["front_default"]

	pokemonlar[pokemonNesnesi.adi] = pokemonNesnesi
	
	i+=1
	if i > 4:
		break

for index in pokemonlar:
	pokemon = pokemonlar[index]
	print(pokemon.adi)

secilen1 = input("1. Oyuncu Pokemon'u Seçin: ")
secilen2 = input("2. Oyuncu Pokemon'u Seçin: ")










































