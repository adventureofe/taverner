from src.sql.species_family.species_family_list import species_family_list


f = {family[0]: index+1 for index, family in enumerate(species_family_list)}

species_type_list = [
    ("typeless", f["none"]),
    ("cat", f["feline"]),
    ("lynx", f["feline"]),
    ("tiger", f["feline"]),
    ("wildcat", f["feline"]),
    ("leopard", f["feline"]),
    ("lion", f["feline"]),
    ("hyena", f["feline"]),
    ("aardvark", f["aardvark"]),

    ("smalldog", f["canine"]),
    ("dog", f["canine"]),
    ("wilddog", f["canine"]),
    ("wolf", f["canine"]),
    ("fox", f["canine"]),
    ("bear", f["canine"])
]
