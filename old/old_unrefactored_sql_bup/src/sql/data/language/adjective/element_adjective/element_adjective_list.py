from sql.generate.element.element_list import element_list
from sql.generate.language.adjective.adjective_list import adjective_list

e = {element[0]: index+1 for index, element in enumerate(element_list)}
a = {adjective[0]: index+1 for index, adjective in enumerate(adjective_list)}

element_adjective_list = [
    (a["alien"], e["alien"]),
    (a["otherworldly"], e["alien"]),
    (a["extraterrestrial"], e["alien"]),
    (a["airy"], e["air"]),
    (a["windy"], e["air"]),
    (a["gusty"], e["air"]),
    (a["chaotic"], e["chaos"]),
    (a["mindboggling"], e["chaos"]),
    (a["electrifying"], e["electricity"]),
    (a["shocking"], e["evil"]),
    (a["evil"], e["evil"]),
    (a["devilish"], e["evil"]),
    (a["demonic"], e["evil"]),
    (a["fiery"], e["fire"]),
    (a["flaming"], e["fire"]),
    (a["flamin"], e["fire"]),
    (a["holy"], e["holiness"]),
    (a["heavenly"], e["holiness"]),
    (a["icy"], e["ice"]),
    (a["freezing"], e["ice"]),
    (a["freezin"], e["ice"]),
    (a["chilling"], e["ice"]),
    (a["chillin"], e["ice"]),
    (a["metal"], e["metal"]),
    (a["metallic"], e["metal"]),
    (a["normal"], e["normal"]),
    (a["magicless"], e["normal"]),
    (a["planty"], e["plant"]),
    (a["leafy"], e["plant"]),
    (a["veggie"], e["plant"]),
    (a["veggy"], e["plant"]),
    (a["poisonous"], e["poison"]),
    (a["poison"], e["poison"]),
    (a["toxic"], e["poison"]),
    (a["radioactive"], e["radiation"]),
    (a["atomic"], e["radiation"]),
    (a["undead"], e["undead"]),
    (a["zombie"], e["undead"]),
    (a["watery"], e["water"]),
    (a["wet"], e["water"]),
    (a["fungal"], e["fungus"]),
    (a["mushroomy"], e["fungus"]),

    *( (a["scruffy"], e[element]) for element in ["air", "chaos", "earth", "electricity", "mutation", "normal", "plant", "poison", "radiation", "undead", "fungus"]),

    *( (a["shapely"], e[element]) for element in ["alien", "air", "chaos", "earth", "evil", "fire", "holiness", "ice", "metal", "mutation", "normal", "plant", "poison", "undead", "water", "fungus"]),

*( (a["shy"], e[element]) for element in ["air", "earth", "ice", "mutation", "normal", "plant", "water", "fungus"]),

    *( (a["silly"], e[element]) for element in ["alien", "chaos", "electricity", "evil", "fire", "mutation", "plant", "poison", "radiation", "undead", "fungus"]),

    *( (a["stocky"], e[element]) for element in ["alien", "air", "earth", "electricity", "fire", "ice", "normal", "plant", "undead", "water", "fungus"]),
 
    *( (a["stalky"], e[element]) for element in ["plant", "fungus"]),

    *( (a["unimportant"], e[element]) for element in ["alien", "air", "chaos", "earth", "electricity", "evil", "fire", "holiness", "ice", "metal", "mutation", "normal", "plant", "poison", "radiation", "undead", "water", "fungus"]),

    *( (a["unkempt"], e[element]) for element in ["air", "chaos", "earth", "electricity", "mutation", "normal", "plant", "poison", "radiation", "undead", "fungus"]),

    *( (a["unslightly"], e[element]) for element in ["alien", "chaos", "evil", "fire", "metal", "mutation", "poison", "radiation", "undead", "fungus"]),

    *( (a["uptight"], e[element]) for element in ["alien", "chaos", "electricity", "evil", "fire", "holiness", "ice", "undead"]),

    *( (a["vast"], e[element]) for element in ["alien", "air", "chaos", "earth", "evil", "fire", "holiness", "ice", "radiation", "undead", "water"]),

    *( (a["wonderful"], e[element]) for element in ["alien", "air", "chaos", "earth", "electricity", "evil", "fire", "holiness", "ice", "metal", "mutation", "normal", "plant", "poison", "radiation", "undead", "water", "fungus"]),

    *( (a["zealous"], e[element]) for element in ["alien", "air", "chaos", "earth", "electricity", "evil", "fire", "holiness", "ice", "metal", "mutation", "normal", "plant", "poison", "radiation", "undead", "water", "fungus"]),

    *( (a["famous"], e[element]) for element in ["alien", "air", "chaos", "earth", "electricity", "evil", "fire", "holiness", "ice", "metal", "mutation", "normal", "plant", "poison", "radiation", "undead", "water", "fungus"]),


    *( (a["fat"], e[element]) for element in ["alien", "chaos", "evil", "fire", "holiness", "mutation", "normal", "undead", "fungus"]),

    *( (a["gentle"], e[element]) for element in ["air", "earth", "fire", "holiness", "ice", "plant", "water", "fungus"]),

    *( (a["glamorous"], e[element]) for element in ["alien", "air", "chaos", "earth", "electricity", "evil", "fire", "holiness", "ice", "metal", "mutation", "normal", "plant", "poison", "radiation", "undead", "water", "fungus"]),

    *( (a["glamorous"], e[element]) for element in ["alien", "air", "chaos", "earth", "electricity", "evil", "fire", "holiness", "ice", "metal", "mutation", "normal", "plant", "poison", "radiation", "undead", "water", "fungus"]),

    *( (a["important"], e[element]) for element in ["alien", "air", "chaos", "earth", "electricity", "evil", "fire", "holiness", "ice", "metal", "mutation", "normal", "plant", "poison", "radiation", "undead", "water", "fungus"]),

    *( (a["interesting"], e[element]) for element in ["alien", "air", "chaos", "earth", "electricity", "evil", "fire", "holiness", "ice", "metal", "mutation", "normal", "plant", "poison", "radiation", "undead", "water", "fungus"]),

    *( (a["uninteresting"], e[element]) for element in ["alien", "air", "chaos", "earth", "electricity", "evil", "fire", "holiness", "ice", "metal", "mutation", "normal", "plant", "poison", "radiation", "undead", "water", "fungus"]),

    *( (a["jolly"], e[element]) for element in ["alien", "chaos", "evil", "holiness", "mutation", "normal", "plant", "undead", "fungus"]),

    *( (a["journied"], e[element]) for element in ["alien", "air", "chaos", "earth", "electricity", "evil", "fire", "holiness", "ice", "metal", "mutation", "normal", "plant", "poison", "radiation", "undead", "water", "fungus"]),

    *( (a["joyful"], e[element]) for element in ["chaos", "earth", "electricity", "holiness", "normal", "plant", "water", "fungus"])

]
