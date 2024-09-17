import sys
import sqlite3
import pandas as pd

from sql.generate.species.species_list import species_list
from sql.generate.move.move_list import move_list
from sql.generate.moveset.moveset_chance.moveset_chance_list import moveset_chance_list

s = {species[2]: index+1 for index, species in enumerate(species_list)}
m = {move[0]: index+1 for index, move in enumerate(move_list)}
ch = {chance: index+1 for index, chance in enumerate(moveset_chance_list)}

#guaranteed, highly un/likely, very un/likely,
# somewhat un/likely equally likely, impossible

species_moveset_list = [
    (s["aardvark"], m["thud"], 0, ch["guaranteed"]),
    (s["aardvark"], m["sand blast"], 0, ch["guaranteed"]),
    (s["bengal tiger"], m["thud"], 0, ch["guaranteed"]),
    (s["siberian tiger"], m["thud"], 0, ch["guaranteed"])
]
