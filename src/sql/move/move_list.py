#!/usr/bin/env python3

from src.sql.element.element_list import element_list
from src.sql.move_type.move_type_list import move_type_list
from src.sql.move_category.move_category_list import move_category_list
from src.sql.chance.chance_list import chance_list

e = {element[0]: index+1 for index, element in enumerate(element_list)}
t = {move_type[0]: index+1 for index, move_type in enumerate(move_type_list)}
c = {category[0]: index+1 for index, category in enumerate(move_category_list)}
ch = {chance[0]: index+1 for index, chance in enumerate(chance_list)}

move_list = [
    # default attack should hit all types. Hitting this locks you into it until the battle is finished
    ("thud", 50, e["typeless"], t["typeless"], c["none"], 0, ch["guaranteed"], "a thud that deals a 1/4 of damage dealt back."),

    # alien physical
    # name  power element     type           category  priority chance description
    ("probe", 50, e["alien"], t["melee"], c["tool"], 1, ch["guaranteed"], "probe target for alien damage"),
    ("plasma fist", 75, e["alien"], t["melee"], c["arm"], 0, ch["guaranteed"], "probe target for alien damage"),
    # alien special
    ("death ray", 50, e["alien"], t["ranged"], c["blast"], 0, ch["guaranteed"], "a harmful ray"),
    ("plasma ball", 60, e["alien"], t["ranged"], c["ball"], 0, ch["guaranteed"], "a burning ball of plasma"),
    # air physical
    ("peck", 50, e["air"], t["melee"], c["beak"], 0, ch["guaranteed"], "peck the target with a sharp beak"),
    ("wing attack", 60, e["air"], t["melee"], c["wing"], 0, ch["guaranteed"], "hit hard from the sky"),
    ("talon slash", 60, e["air"], t["melee"], c["claw"], 0, ch["guaranteed"], "attack from above with sharp talons"),
    ("drilling peck", 80, e["air"], t["melee"], c["beak"], 0, ch["highly likely"], "peck the target with a drill-like beak"),
    # air special
    ("gust", 50, e["air"], t["ranged"], c["blast"], 0, ch["guaranteed"], "a harmful gust"),
    ("wind bolt", 60, e["air"], t["ranged"], c["bolt"], 0, ch["guaranteed"], "a powerful bolt of wind shot like an arrow"),
    ("hurricane", 70, e["air"], t["ranged"], c["wing"], 0, ch["guaranteed"], "a fiercesome wind"),
    ("tornado", 95, e["air"], t["ranged"], c["wing"], 0, ch["very likely"], "a fiercesome wind"),
    # chaos physical
    ("flabbergast", 70, e["chaos"], t["melee"], c["body"], 0, ch["guaranteed"], "the target is hit with chaotic circumstances"),
    ("chaotic fit", 95, e["chaos"], t["melee"], c["body"], 0, ch["somewhat likely"], "the target is hit with chaotic circumstances"),
    # chaos special
    ("discombobulate", 70, e["chaos"], t["ranged"], c["body"], 0, ch["guaranteed"], "blow the targets mind with chaos energy"),
    ("chaos beam", 55, e["chaos"], t["ranged"], c["beam"], 0, ch["guaranteed"], "beam pure chaos into the target's mind"),
    # earth physical
    ("earthquake", 100, e["earth"], t["melee"], c["weight"], 0, ch["guaranteed"], "tremendously shake the earth"),
    ("bulldoze", 60, e["earth"], t["melee"], c["weight"], 0, ch["highly likely"], "stomp all in your path"),
    # earth special
    ("sand blast", 55, e["earth"], t["ranged"], c["blast"], 0, ch["guaranteed"], "sand blasts target"),
    ("mud bomb", 65, e["earth"], t["ranged"], c["ball"], 0, ch["guaranteed"], "attack target with ball of mud"),
    # electricity physical
    ("thunder punch", 75, e["electricity"], t["melee"], c["arm"], 0, ch["guaranteed"], "may shock target %10"),
    ("lightning kick", 75, e["electricity"], t["melee"], c["arm"], 0, ch["guaranteed"], "may shock target %10"),
    # electricity special
    ("thunder bolt", 90, e["electricity"], t["ranged"], c["bolt"], 0, ch["guaranteed"], "may shock target %10"),
    ("electroball", 75, e["electricity"], t["ranged"], c["ball"], 0, ch["guaranteed"], "may shock target %10"),
    # evil physical
    ("sucker punch", 70, e["evil"], t["melee"], c["arm"], 1, ch["guaranteed"], "a disgraceful blow"),
    ("bite", 60, e["evil"], t["melee"], c["tooth"], 0, ch["guaranteed"], "a disgraceful blow"),
    ("backstab", 100, e["evil"], t["melee"], c["tool"], 0, ch["very likely"], "a disgraceful blow"),
    # evil special
    ("dark pulse", 60, e["evil"], t["ranged"], c["blast"], 0, ch["guaranteed"], "a disgraceful blow"),
    ("arrow in back", 65, e["evil"], t["ranged"], c["bolt"], 0, ch["highly likely"], "a disgraceful blow"),
    # fire physical
    ("fire punch", 75, e["fire"], t["melee"], c["arm"], 0, ch["guaranteed"], "a flaming punch that can burn 33%"),
    ("blaze kick", 85, e["fire"], t["melee"], c["leg"], 0, ch["guaranteed"], "a flaming kick that can burn 33%"),
    # fire special
    ("flamethrower", 90, e["fire"], t["ranged"], c["spit"], 0, ch["guaranteed"], "spit flames over target"),
    ("ember", 50, e["fire"], t["ranged"], c["blast"], 0, ch["guaranteed"], "spit flames over target"),
    # holiness physical
    ("holy punch", 75, e["holiness"], t["typeless"], c["arm"], 0, ch["guaranteed"], "a holy punch ignores type"),
    ("shield bash", 65, e["holiness"], t["melee"], c["tool"], 0, ch["highly likely"], "a holy punch ignores type"),
    # holiness special
    ("smite", 55, e["holiness"], t["ranged"], c["bolt"], 0, ch["guaranteed"], "smite foes down"),
    ("beam of light", 70, e["holiness"], t["ranged"], c["beam"], 0, ch["guaranteed"], "the light of judgement beams down"),
    # ice physical
    ("ice punch", 75, e["ice"], t["melee"], c["arm"], 0, ch["guaranteed"],  "a freezing punch that can freeze 10%"),
    ("icicle spear", 50, e["ice"], t["melee"], c["bolt"], 1, ch["very likely"],  "a freezing icicle pierces target"),
    # ice special
    ("ice beam", 90, e["ice"], t["ranged"], c["beam"], 0, ch["guaranteed"],  "a freezing beam"),
    ("snowball", 55, e["ice"], t["ranged"], c["ball"], 1, ch["very likely"],  "a freezing beam"),
    # metal physical
    ("bullet punch", 50, e["metal"], t["melee"], c["arm"], 1, ch["guaranteed"], "a heavy, metallic punch with increased priority"),
    ("metal slam", 70, e["metal"], t["melee"], c["weight"], 0, ch["highly likely"], "a heavy, metallic punch with increased priority"),
    # metal special
    ("shoot", 50, e["metal"], t["ranged"], c["bolt"], 1, ch["guaranteed"], "fire metal bolts at target"),
    ("shrapnel", 80, e["metal"], t["ranged"], c["blast"], 0, ch["highly likely"], "fires shards of metal at the opponent"),
    # mutation physical
    ("tentacle smash", 80, e["mutation"], t["melee"], c["tentacle"], 0, ch["highly likely"], "whip with a mutated tentacle"),
    ("tentacle suck", 60, e["mutation"], t["melee"], c["tentacle"], 0, ch["very likely"], "whip with a mutated tentacle"),
    # mutation special
    ("telekenesis", 90, e["mutation"], t["ranged"], c["mind"], 0, ch["highly likely"], "throw an object telekinetically at the target"),
    ("tentacle spit", 65, e["mutation"], t["ranged"], c["tentacle"], 0, ch["highly likely"], "throw an object telekinetically at the target"),
    # normal physical
    ("tackle", 50, e["normal"], t["melee"], c["body"], 0, ch["guaranteed"], "tackle the target"),
    ("mega punch", 80, e["normal"], t["melee"], c["arm"], 0, ch["guaranteed"], "a powerful punch"),
    ("body slam", 85, e["normal"], t["melee"], c["weight"], 0, ch["guaranteed"], "may paralyze 30%"),
    ("fake out", 40, e["normal"], t["melee"], c["body"], 3, ch["guaranteed"], "increased priority"),
    ("extreme speed", 80, e["normal"], t["melee"], c["body"], 2, ch["guaranteed"], "increased priority"),
    # normal special
    ("sonic boom", 50, e["normal"], t["ranged"], c["blow"], 0, ch["guaranteed"], "tackle the target"),
    ("mind bomb", 70, e["normal"], t["ranged"], c["blast"], 0, ch["highly likely"], "tackle the target"),
    # plant physical
    ("tropical kick", 70, e["plant"], t["melee"], c["leg"], 0, ch["guaranteed"], "a tropical kick"),
    ("stick whack", 70, e["plant"], t["melee"], c["tool"], 0, ch["highly likely"], "a tropical kick"),
    # plant special
    ("nature beam", 70, e["plant"], t["ranged"], c["beam"], 0, ch["guaranteed"], "beam power of naure into target"),
    ("vine whip", 75, e["plant"], t["ranged"], c["whip"], 0, ch["highly likely"], "beam power of naure into target"),
    # poison physical
    ("poison fang", 70, e["poison"], t["melee"], c["tooth"], 0, ch["guaranteed"], "bite user with venomous fangs"),
    ("poison jab", 80, e["poison"], t["melee"], c["tool"], 0, ch["highly likely"], "bite user with venomous fangs"),
    # poison special
    ("poison dart", 70, e["poison"], t["ranged"], c["blow"], 2, ch["guaranteed"], "quickly shoot a poison dart"),
    ("ink", 80, e["poison"], t["ranged"], c["tentacle"], 0, ch["highly likely"], "spit water into the face of target"),
    # radiation physical
    ("atomic punch", 70, e["radiation"], t["melee"], c["arm"], 0, ch["guaranteed"], "an atom splitting punch"),
    ("atomic kick", 60, e["radiation"], t["melee"], c["leg"], 0, ch["guaranteed"], "an atom splitting punch"),
    # radication special
    ("atomic blast", 80, e["radiation"], t["ranged"], c["blast"], 0, ch["highly likely"], "an atom splitting punch"),
    ("atom bomb", 100, e["radiation"], t["ranged"], c["blow"], 0, ch["likely"], "an atom splitting punch"),
    # undead physical
    ("shadow punch", 60, e["undead"], t["melee"], c["arm"], 0,  ch["guaranteed"], "a ghostly punch"),
    ("cannibalise", 70, e["undead"], t["melee"], c["tooth"], 0, ch["guaranteed"],  "a ghostly punch"),
    ("shadow punch", 60, e["undead"], t["melee"], c["arm"], 0, ch["guaranteed"],  "a ghostly punch"),
    # undead special
    ("shadow ball", 60, e["undead"], t["ranged"], c["ball"], 0, ch["highly likely"],  "a ball of ghostly energy strikes the target"),
    ("blood spit", 60, e["undead"], t["ranged"], c["spit"], 0, ch["highly likely"],  "a ball of ghostly energy strikes the target"),
    # water physica
    ("aqua punch", 75, e["water"], t["melee"], c["arm"], 0, ch["guaranteed"], "a salty punch"),
    ("aqua tentacle", 65, e["water"], t["melee"], c["tentacle"], 0, ch["highly likely"], "a salty punch"),
    ("aqua tail", 70, e["water"], t["melee"], c["arm"], 0, ch["guaranteed"], "a salty punch"),
    # water special
    ("water gun", 50, e["water"], t["ranged"], c["spit"], 0, ch["guaranteed"], "spit water into the face of target"),
    ("tidal wave", 80, e["water"], t["ranged"], c["body"], 0, ch["highly likely"], "crash a huge wave on the target"),
    # fungus physical
    ("mushroom punch", 55, e["fungus"], t["melee"], c["arm"], 0, ch["guaranteed"], "a disgusting shroomy punch"),
    ("mushroom kick", 75, e["fungus"], t["melee"], c["leg"], 0, ch["very likely"], "a disgusting shroomy kick"),
    # fungus special
    ("spore cannon", 55, e["fungus"], t["ranged"], c["blow"], 0,  ch["guaranteed"], "fire harmful spores"),
    ("mushroom blast", 65, e["fungus"], t["ranged"], c["blast"], 0,  ch["guaranteed"], "fire harmful spores")
]
