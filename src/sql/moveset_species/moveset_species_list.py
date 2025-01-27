from src.sql.chance.chance_list import chance_list
from src.sql.species.species_list import species_list
from src.sql.move.move_list import move_list

c = {chance[0]: index+1 for index, chance in enumerate(chance_list)}
s = {species[3]: index+1 for index, species in enumerate(species_list)}
m = {move[0]: index+1 for index, move in enumerate(move_list)}


moveset_species_list = [
    (s["british shorthair"], m["thud"], 0, c["guaranteed"]),
    (s["eurasian lynx"], m["thud"], 0, c["guaranteed"]),
    (s["siberian tiger"], m["thud"], 0, c["guaranteed"]),
    (s["siamese"], m["thud"], 0, c["guaranteed"]),
    (s["ocelot"], m["thud"], 0, c["guaranteed"]),
    (s["snow leopard"], m["thud"], 0, c["guaranteed"]),
]
