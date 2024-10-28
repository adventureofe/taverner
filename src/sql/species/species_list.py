from src.sql.species_type.species_type_list import species_type_list
from src.sql.species_family.species_family_list import species_family_list

t = {type: index+1 for index, type in enumerate(species_type_list)}
f = {family: index+1 for index, family in enumerate(species_family_list)}

species_list = [
    (f["shrew"], t["aardvark"], "aardvark", 600, 760, 40000, 65000),
    (f["feline"], t["tiger"], "bengal tiger", 900, 1100, 100000, 260000),
    (f["feline"], t["tiger"], "siberian tiger", 750, 1070, 118000, 318000),
    (f["equine"], t["zebra"], "zebra", 1200, 1500, 350000, 450000),
    (f["canine"], t["dog"], "german shepherd", 550, 650, 22000, 40000),
    (f["canine"], t["dog"], "labrador retriever", 550, 620, 25000, 36000),
    (f["canine"], t["dog"], "dachshund", 200, 230, 9000, 12000),
    (f["feline"], t["cat"], "british shorthair", 300, 355, 3200, 7700),
    (f["feline"], t["cat"], "siamese", 290, 310,2500, 6000),
    (f["feline"], t["cat"], "sphynx", 200, 250, 3500, 5000),
    (f["feline"], t["cat"], "scottish fold", 200, 250, 4100, 5900),
    (f["rodent"], t["squirrel"], "red squirrel", 190, 230, 200, 500),
    (f["rodent"], t["squirrel"], "grey squirrel", 200, 280, 400, 700),
    (f["canine"], t["bear"], "sun bear", 1000, 1400, 27000, 65000),
    (f["canine"], t["bear"], "grizzly bear", 900, 1500, 100000, 600000),
    (f["canine"], t["bear"], "black bear", 1000, 1200, 41000, 250000),
    (f["canine"], t["bear"], "polar bear", 1220, 1600, 400000, 800000),
    (f["canine"], t["bear"], "panda bear", 1200, 1800, 104000, 113000),
    (f["canine"], t["fox"], "red fox", 560, 820, 3600, 7700),
    (f["canine"], t["fox"], "grey fox", 530, 810, 3200, 6400),
    (f["canine"], t["fox"], "arctic fox", 500, 850, 2500, 5000),
    (f["canine"], t["fox"], "fennec fox", 350, 400, 900, 1400),
    (f["canine"], t["fox"], "tibetan fox", 500, 700, 4000, 5500)
]
