from src.sql.species_type.species_type_list import species_type_list

t = {type[0]: index+1 for index, type in enumerate(species_type_list)}

species_list = [
#   type            ln ps  name1                        name2                  height(mm) weight(g)
   (t["cat"],       1, 1, "british shorthair",          "british shorthair",   300, 460,  3200,   7700),
   (t["lynx"],      1, 2, "eurasian lynx",              "lynx lynx",           600, 750,  18000,  28000),
   (t["tiger"],     1, 3, "siberian tiger",             "amur tiger",          750, 1070, 120000, 222000),

   (t["cat"],       2, 1, "siamese",                    "maeo sayam",          290, 310,  2500,   6000),
   (t["wild cat"],  2, 2, "ocelot",                     "leopardus pardalis",  380, 510,  7000,   15500),
   (t["leopard"],   2, 3, "snow leopard",               "panthera uncia",      550, 650,  40000,  55000),

   (t["cat"],       3, 1, "maine coon",                 "maine coon",          250, 400,  4800,   9500),
   (t["lynx"],      3, 2, "bobcat",                     "lynx rufus",          460, 640,  6400,   18000),
   (t["lion"],      3, 3, "lion",                       "panthera leo",        900, 1200, 130000, 190000),

   (t["small dog"], 4, 1, "dachshund",                  "wiener dog",          200, 230,  9000,   12000),
   (t["dog"],       4, 2, "german shorthaired pointer", "deutsch kurzhaar",    584, 635,  25000,  32000),
   (t["wild dog"],  4, 3, "golden jackal",              "canis aureus",        350, 450,  10000,  15000),

   (t["small dog"], 5, 1, "miniature pinscher ",        "zwergpinscher",       250, 300,  4000,   6000),
   (t["dog"],       5, 2, "dobermann",                  "dobermann",           630, 720,  35000,  45000),
   (t["wild dog"],  5, 3, "african wild dog",           "lycaon pictus",       600, 750, 18000,  36000),

   (t["small dog"], 6, 1, "Bichon Frisé",               "Bichon à Poil Frisé", 230, 300, 4500, 5000),
   (t["dog"],       6, 2, "Kangal Shepherd Dog",        "Kangal Çoban Köpeği", 700, 800, 48000, 60000),
   (t["bear"],      6, 3, "grizzly bear",           "Ursus arctos horribilis", 900, 1500, 100000, 600000),

   (t["small dog"], 7, 1, "pomeranian",                 "pome",                180, 240, 1400, 3200),
   (t["dog"],       7, 2, "alaskan malamute",           "alaskan malamute",    560, 660, 34000, 39000),
   (t["wolf"],      7, 3, "gray wolf",                  "canis lupus",         800, 850, 55000, 80000),
]
#   (f["shrew"], t["aardvark"], "aardvark", 600, 760, 40000, 65000),
#   (f["feline"], t["tiger"], "bengal tiger", 900, 1100, 100000, 260000),
#   (f["equine"], t["zebra"], "zebra", 1200, 1500, 350000, 450000),
#   (f["canine"], t["dog"], "german shepherd", 550, 650, 22000, 40000),
#   (f["canine"], t["dog"], "labrador retriever", 550, 620, 25000, 36000),
#   (f["feline"], t["cat"], 3, "sphynx", 200, 250, 3500, 5000),
#   (f["feline"], t["cat"], 4, "scottish fold", 200, 250, 4100, 5900),
#   (f["rodent"], t["squirrel"], "red squirrel", 190, 230, 200, 500),
#   (f["rodent"], t["squ]irrel"], "grey squirrel", 200, 280, 400, 700),
#   (f["canine"], t["bear"], "sun bear", 1000, 1400, 27000, 65000),
#   (f["canine"], t["bear"], "grizzly bear", 900, 1500, 100000, 600000),
#   (f["canine"], t["bear"], "polar bear", 1220, 1600, 400000, 800000),
#    (f["canine"], t["bear"], "panda bear", 1200, 1800, 104000, 113000),
#   (f["canine"], t["fox"], "red fox", 560, 820, 3600, 7700),
#   (f["canine"], t["fox"], "grey fox", 530, 810, 3200, 6400),
#   (f["canine"], t["fox"], "arctic fox", 500, 850, 2500, 5000),
#   (f["canine"], t["fox"], "fennec fox", 350, 400, 900, 1400),
#   (f["canine"], t["fox"], "tibetan fox", 500, 700, 4000, 5500)
