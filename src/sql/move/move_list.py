#!/usr/bin/env python3

from src.sql.element.element_list import element_list
from src.sql.move_type.move_type_list import move_type_list
from src.sql.move_category.move_category_list import move_category_list

e = {element[0]: index+1 for index, element in enumerate(element_list)}
t = {move_type[0]: index+1 for index, move_type in enumerate(move_type_list)}
c = {category[0]: index+1 for index, category in enumerate(move_category_list)}

move_list = [
    # default attack should hit all types. Hitting this locks you into it until the battle is finished
    ("thud", 50, e["normal"], t["typeless"], c["none"], 0, "a thud that deals a 1/4 of damage dealt back."),

    # alien physical
    ("probe", 50, e["alien"], t["physical"], c["arm"], 0, "probe the enemy for alien damage"),
    ("plasma fist", 70, e["alien"], t["physical"], c["arm"], 0, "probe the enemy for alien damage"),
    # alien special
    ("death ray", 50, e["alien"], t["special"], c["bolt"], 0, "a harmful ray"),
    ("plasma ball", 50, e["alien"], t["special"], c["bolt"], 0, "a harmful ray"),
    # air physical
    ("wing attack", 60, e["air"], t["physical"], c["wing"], 0, "a harmful gust"),
    # air special
    ("wind bolt", 70, e["air"], t["special"], c["bolt"], 0, "a harmful gust"),
    ("gust", 40, e["air"], t["special"], c["wing"], 0, "a harmful gust"),
    ("hurricane", 70, e["air"], t["special"], c["wing"], 0, "a harmful gust"),
    # chaos physical
    # chaos special
    # earth physical
    # earth special
    ("sand blast", 55, e["earth"], t["special"], c["blast"], 0, "sand blasts opponent"),
    # electricity physical
    ("thunder punch", 75, e["electricity"], t["physical"], c["arm"], 0, "may shock opponent %10"),
    # electricity special
    ("thunder bolt", 90, e["electricity"], t["special"], c["bolt"], 0, "may shock opponent %10"),
    # evil physical
    ("sucker punch", 70, e["evil"], t["physical"], c["arm"], 1, "a disgraceful blow"),
    ("bite", 60, e["evil"], t["physical"], c["bite"], 0, "a disgraceful blow"),
    # evil special
    # fire physical
    ("fire punch", 75, e["fire"], t["physical"], c["arm"], 0, "a flaming punch that can burn 33%"),
    ("blaze kick", 85, e["fire"], t["physical"], c["leg"], 0, "a flaming punch that can burn 33%"),
    # fire special
    # holiness physical
    ("holy punch", 75, e["holiness"], t["typeless"], c["arm"], 0, "a holy punch ignores type"),
    # holiness special
    ("smite", 70, e["holiness"], t["special"], c["bolt"], 0, "smite foes down"),
    # ice physical
    ("ice punch", 75, e["ice"], t["physical"], c["arm"], 0,  "a freezing punch that can freeze 10%"),
    # ice special
    # metal physical
    ("bullet punch", 40, e["metal"], t["physical"], c["arm"], 1, "priority"),
    # metal special
    # mutation physical
    # mutation special
    # normal physical
    ("mega punch", 80, e["normal"], t["physical"], c["arm"], 0, "a powerful punch"),
    ("body slam", 85, e["normal"], t["physical"], c["body"], 0, "may paralyze 30%"),
    ("fake out", 40, e["normal"], t["physical"], c["body"], 3, "increased priority"),
    ("extreme speed", 80, e["normal"], t["physical"], c["body"], 2, "increased priority"),
    # normal special
    # plant physical
    ("tropical kick", 70, e["plant"], t["physical"], c["leg"], 0, "a tropical kick"),
    # plant special
    # poison physical
    # poison special
    ("poison dart", 70, e["poison"], t["special"], c["blow"], 2, "quickly shoot a poison dart"),
    # radiation physical
    ("atomic punch", 70, e["radiation"], t["physical"], c["arm"], 0, "an atom splitting punch"),
    # radication special
    # undead physical
    ("shadow punch", 60, e["undead"], t["physical"], c["arm"], 0,  "a ghostly punch"),
    # undead special
    # water physical
    ("aqua punch", 75, e["water"], t["physical"], c["arm"], 0, "a salty punch"),
    # water special
    # fungus physical
    ("mushroom punch", 55, e["fungus"], t["physical"], c["arm"], 0, "a disgusting shroomy punch"),
    # fungus special
    ("spore cannon", 55, e["fungus"], t["special"], c["blow"], 0, "fire harmful spores")
]
