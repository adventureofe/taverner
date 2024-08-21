from sql.generate.colour.colour_list import colour_list
from sql.generate.species.species_type.species_type_list import species_type_list
from sql.generate.species.species_family.species_family_list import species_family_list
c = {color[0]: index+1 for index, color in enumerate(colour_list)}
st = {species_type: index+1 for index, species_type in enumerate(species_type_list)}
sf = {species_family: index+1 for index, species_family in enumerate(species_family_list)}

species_list = [
    (sf["shrew"], st["aardvark"], "aardvark", c["brown"], c["brown"], 600, 760, 40000, 65000),
    (sf["feline"], st["tiger"], "bengal tiger", c["orange"], c["black"], 900, 1100, 100000, 260000),
    (sf["feline"], st["tiger"], "siberian tiger", c["orange"], c["black"], 750, 1070, 118000, 318000),
    (sf["equine"], st["zebra"], "zebra", c["white"], c["black"], 1200, 1500, 350000, 450000),
    (sf["canine"], st["dog"], "german shepherd", c["brown"], c["black"], 550, 650, 22000, 40000),
    (sf["canine"], st["dog"], "labrador retriever", c["yellow"], c["brown"], 550, 620, 25000, 36000),
    (sf["canine"], st["dog"], "dachshund", c["black"], c["brown"], 200, 230, 9000, 12000),
    (sf["feline"], st["cat"], "british shorthair", c["black"], c["white"], 300, 355, 3200, 7700),
    (sf["feline"], st["cat"], "siamese", c["white"], c["white"], 290, 310,2500, 6000),
    (sf["feline"], st["cat"], "sphynx", c["white"], c["yellow"], 200, 250, 3500, 5000),
    (sf["feline"], st["cat"], "scottish fold", c["white"], c["yellow"], 200, 250, 4100, 5900),
    (sf["rodent"], st["squirrel"], "red squirrel", c["red"], c["red"], 190, 230, 200, 500),
    (sf["rodent"], st["squirrel"], "grey squirrel", c["grey"], c["grey"], 200, 280, 400, 700),
    (sf["canine"], st["bear"], "sun bear", c["black"], c["yellow"], 1000, 1400, 27000, 65000),
    (sf["canine"], st["bear"], "grizzly bear", c["brown"], c["brown"], 900, 1500, 100000, 600000),
    (sf["canine"], st["bear"], "black bear", c["black"], c["black"], 1000, 1200, 41000, 250000),
    (sf["canine"], st["bear"], "polar bear", c["white"], c["white"], 1220, 1600, 400000, 800000),
    (sf["canine"], st["bear"], "panda bear", c["white"], c["black"], 1200, 1800, 104000, 113000),
    (sf["canine"], st["fox"], "red fox", c["red"], c["red"], 560, 820, 3600, 7700),
    (sf["canine"], st["fox"], "grey fox", c["grey"], c["grey"], 530, 810, 3200, 6400),
    (sf["canine"], st["fox"], "arctic fox", c["white"], c["grey"], 500, 850, 2500, 5000),
    (sf["canine"], st["fox"], "fennec fox", c["yellow"], c["yellow"], 350, 400, 900, 1400),
    (sf["canine"], st["fox"], "tibetan fox", c["yellow"], c["grey"], 500, 700, 4000, 5500)
]
