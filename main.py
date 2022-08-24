from genericpath import exists
from db.database import Database
from helper.WriteAJson import writeAJson

db = Database(database="pokedex", collection="pokemons")

# Pokemons tipo grass ou poison com fraqueza de flying ou fogo
type = ["Grass", "Poison"]
weaknesses = ["Flying", "Fire"]
pokemons1 = db.executeQuery({"type": {"$in": type}, "weaknesses": {"$in": weaknesses}})
writeAJson(pokemons1,"tipo_com_fraqueza")

# Pokemons sem evolucao
pokemons2 = db.executeQuery({"next_evolution": {"$exists": False} })
writeAJson(pokemons2,"sem_evolucao")

# Pokemon numero 135
pokemons3 = db.executeQuery({"num": "135"})
writeAJson(pokemons3,"num_135")

# Pokemons com apenas 1 tipo de fraqueza
pokemons4 = db.executeQuery({"weaknesses": {"$size": 1}})
writeAJson(pokemons4,"uma_fraqueza")

# Pokemons do tipo = fogo ou fraqueza = fogo
pokemons5 = db.executeQuery({"$or": [{"type": "Fire"},{"weaknesses": "Fire"}]})
writeAJson(pokemons5,"tipo_ou_fraqueza")