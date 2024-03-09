# colour list (1) pink (2) magenta (3) silver (4) orange (5) brown (6) yellow (7) black (8) red (9) white
# (10) cyan (11) dark grey (12) maroon (13)


from enum import Enum

class Col(Enum):
    PINK = 1
    MAGENTA = 2
    SILVER = 3
    ORANGE = 4
    BROWN = 5
    YELLOW = 6
    BLACK = 7
    RED = 8
    WHITE = 9
    CYAN = 10
    DGREY = 11
    MAROON = 12
    GREY = 13
    GREEN = 14
    PURPLE = 15
    LIME = 16
    DGREEN = 17 
    BLUE = 18
    GOLD = 19

class Adj(Enum):
    AERIAL= 1
    AESTHETIC= 2
    ANGELIC = 3
    ASTONISHING = 4
    BEWILDERING = 5
    BITTER = 6
    BLUSH = 7
    BOLD = 8
    BRASH = 9
    BRIGHT = 10
    BRILLIANT = 11
    CALM = 12
    CALMING = 13
    CHARMING = 14
    CHEERFUL = 15
    CHILL = 16
    CHILLY = 17
    CLASSIC = 18
    CLOUDY = 19
    COLD = 20
    CONFIDENT = 21
    COOL = 22
    COSMIC = 23
    COSY = 24
    CRISP = 25
    CRISPY = 26
    CURIOUS = 27
    DAINTY = 28
    DANK = 29
    DARING = 30
    DAZZLING = 31
    DEEP = 32
    DELICATE = 33
    DISTINCTIVE = 34
    DRAMATIC = 35
    DREAMY = 36
    EARTHY = 37
    ELEGANT = 38
    ENCHANTING = 39
    ENERGETIC = 40
    EXPRESSIVE = 41
    BEAUTIFUL = 42

c = {col.name.lower(): col.value for col in Col}

a = {adj.name.lower(): adj.value for adj in Adj}

colour_adjective_fill_list = [
    (a["aerial"], c["blue"]),

    (a["aesthetic"], c["pink"]),
    (a["aesthetic"], c["magenta"]),
    (a["aesthetic"], c["silver"]),
    (a["aesthetic"], c["orange"]),
    (a["aesthetic"], c["brown"]),
    (a["aesthetic"], c["yellow"]),
    (a["aesthetic"], c["black"]),
    (a["aesthetic"], c["red"]),
    (a["aesthetic"], c["white"]),
    (a["aesthetic"], c["cyan"]),
    (a["aesthetic"], c["dgrey"]),
    (a["aesthetic"], c["maroon"]),
    (a["aesthetic"], c["grey"]),
    (a["aesthetic"], c["green"]),
    (a["aesthetic"], c["purple"]),
    (a["aesthetic"], c["lime"]),
    (a["aesthetic"], c["dgreen"]),
    (a["aesthetic"], c["blue"]),
    (a["aesthetic"], c["gold"]),

    (a["angelic"], c["white"]),

    (a["astonishing"], c["pink"]),
    (a["astonishing"], c["magenta"]),
    (a["astonishing"], c["silver"]),
    (a["astonishing"], c["orange"]),
    (a["astonishing"], c["yellow"]),
    (a["astonishing"], c["black"]),
    (a["astonishing"], c["red"]),
    (a["astonishing"], c["white"]),
    (a["astonishing"], c["cyan"]),
    (a["astonishing"], c["purple"]),
    (a["astonishing"], c["lime"]),
    (a["astonishing"], c["blue"]),
    (a["astonishing"], c["gold"]),

    (a["bewildering"], c["pink"]),
    (a["bewildering"], c["magenta"]),
    (a["bewildering"], c["orange"]),
    (a["bewildering"], c["brown"]),
    (a["bewildering"], c["yellow"]),
    (a["bewildering"], c["black"]),
    (a["bewildering"], c["red"]),
    (a["bewildering"], c["cyan"]),
    (a["bewildering"], c["maroon"]),
    (a["bewildering"], c["green"]),
    (a["bewildering"], c["purple"]),
    (a["bewildering"], c["lime"]),
    (a["bewildering"], c["dgreen"]),
    (a["bewildering"], c["blue"]),
    (a["bewildering"], c["gold"]),

    (a["bitter"], c["brown"]),
    (a["bitter"], c["yellow"]),
    (a["bitter"], c["white"]),
    (a["bitter"], c["dgrey"]),
    (a["bitter"], c["grey"]),
    (a["bitter"], c["lime"]),


    (a["blush"], c["pink"]),
    (a["blush"], c["red"]),

    (a["bold"], c["pink"]),
    (a["bold"], c["magenta"]),
    (a["bold"], c["orange"]),
    (a["bold"], c["brown"]),
    (a["bold"], c["yellow"]),
    (a["bold"], c["black"]),
    (a["bold"], c["red"]),
    (a["bold"], c["cyan"]),
    (a["bold"], c["maroon"]),
    (a["bold"], c["green"]),
    (a["bold"], c["purple"]),
    (a["bold"], c["lime"]),
    (a["bold"], c["blue"]),
    (a["bold"], c["gold"]),

    (a["brash"], c["pink"]),
    (a["brash"], c["magenta"]),
    (a["brash"], c["silver"]),
    (a["brash"], c["brown"]),
    (a["brash"], c["black"]),
    (a["brash"], c["red"]),
    (a["brash"], c["dgrey"]),
    (a["brash"], c["maroon"]),
    (a["brash"], c["grey"]),
    (a["brash"], c["green"]),
    (a["brash"], c["purple"]),
    (a["brash"], c["lime"]),
    (a["brash"], c["dgreen"]),
    (a["brash"], c["blue"]),
    (a["brash"], c["gold"]),

    (a["bright"], c["pink"]),
    (a["bright"], c["magenta"]),
    (a["bright"], c["silver"]),
    (a["bright"], c["orange"]),
    (a["bright"], c["yellow"]),
    (a["bright"], c["red"]),
    (a["bright"], c["white"]),
    (a["bright"], c["cyan"]),
    (a["bright"], c["grey"]),
    (a["bright"], c["green"]),
    (a["bright"], c["purple"]),
    (a["bright"], c["lime"]),
    (a["bright"], c["blue"]),
    (a["bright"], c["gold"]),

    (a["brilliant"], c["pink"]),
    (a["brilliant"], c["silver"]),
    (a["brilliant"], c["orange"]),
    (a["brilliant"], c["brown"]),
    (a["brilliant"], c["yellow"]),
    (a["brilliant"], c["black"]),
    (a["brilliant"], c["red"]),
    (a["brilliant"], c["white"]),
    (a["brilliant"], c["green"]),
    (a["brilliant"], c["purple"]),
    (a["brilliant"], c["blue"]),
    (a["brilliant"], c["gold"]),

    (a["calm"], c["blue"]),

    (a["calming"], c["blue"]),

    (a["cheerful"], c["pink"]),
    (a["cheerful"], c["magenta"]),
    (a["cheerful"], c["silver"]),
    (a["cheerful"], c["orange"]),
    (a["cheerful"], c["yellow"]),
    (a["cheerful"], c["red"]),
    (a["cheerful"], c["white"]),
    (a["cheerful"], c["maroon"]),
    (a["cheerful"], c["green"]),
    (a["cheerful"], c["purple"]),
    (a["cheerful"], c["blue"]),
    (a["cheerful"], c["gold"]),

    (a["chill"], c["silver"]),
    (a["chill"], c["black"]),
    (a["chill"], c["white"]),
    (a["chill"], c["cyan"]),
    (a["chill"], c["lime"]),
    (a["chill"], c["blue"]),

    (a["chilly"], c["silver"]),
    (a["chilly"], c["black"]),
    (a["chilly"], c["white"]),
    (a["chilly"], c["cyan"]),
    (a["chilly"], c["lime"]),
    (a["chilly"], c["blue"]),

    (a["classic"], c["silver"]),
    (a["classic"], c["black"]),
    (a["classic"], c["red"]),
    (a["classic"], c["white"]),
    (a["classic"], c["blue"]),
    (a["classic"], c["gold"]),

    (a["cloudy"], c["lime"]),
    (a["cloudy"], c["white"]),

    (a["cold"], c["silver"]),
    (a["cold"], c["white"]),
    (a["cold"], c["black"]),
    (a["cold"], c["cyan"]),
    (a["cold"], c["dgrey"]),
    (a["cold"], c["grey"]),
    (a["cold"], c["blue"]),
    (a["cold"], c["gold"]),

    (a["confident"], c["pink"]),
    (a["confident"], c["magenta"]),
    (a["confident"], c["silver"]),
    (a["confident"], c["orange"]),
    (a["confident"], c["brown"]),
    (a["confident"], c["yellow"]),
    (a["confident"], c["black"]),
    (a["confident"], c["red"]),
    (a["confident"], c["white"]),
    (a["confident"], c["cyan"]),
    (a["confident"], c["dgrey"]),
    (a["confident"], c["maroon"]),
    (a["confident"], c["grey"]),
    (a["confident"], c["green"]),
    (a["confident"], c["purple"]),
    (a["confident"], c["lime"]),
    (a["confident"], c["dgreen"]),
    (a["confident"], c["blue"]),
    (a["confident"], c["gold"]),

    (a["cool"], c["silver"]),
    (a["cool"], c["yellow"]),
    (a["cool"], c["black"]),
    (a["cool"], c["white"]),
    (a["cool"], c["cyan"]),
    (a["cool"], c["grey"]),
    (a["cool"], c["green"]),
    (a["cool"], c["lime"]),
    (a["cool"], c["dgreen"]),
    (a["cool"], c["blue"]),
    (a["cool"], c["gold"]),

    (a["cosmic"], c["black"]),
    
    (a["cosy"], c["brown"]),

    (a["crisp"], c["silver"]),
    (a["crisp"], c["white"]),
    (a["crisp"], c["lime"]),
    (a["crisp"], c["blue"]),
    (a["crisp"], c["gold"]),

    (a["crispy"], c["brown"]),
    (a["crispy"], c["yellow"]),
    (a["crispy"], c["gold"]),

    (a["curious"], c["pink"]),
    (a["curious"], c["magenta"]),
    (a["curious"], c["silver"]),
    (a["curious"], c["orange"]),
    (a["curious"], c["brown"]),
    (a["curious"], c["yellow"]),
    (a["curious"], c["black"]),
    (a["curious"], c["red"]),
    (a["curious"], c["white"]),
    (a["curious"], c["cyan"]),
    (a["curious"], c["dgrey"]),
    (a["curious"], c["maroon"]),
    (a["curious"], c["grey"]),
    (a["curious"], c["green"]),
    (a["curious"], c["purple"]),
    (a["curious"], c["lime"]),
    (a["curious"], c["dgreen"]),
    (a["curious"], c["blue"]),
    (a["curious"], c["gold"]),

    (a["dainty"], c["pink"]),
    (a["dainty"], c["magenta"]),
    (a["dainty"], c["silver"]),
    (a["dainty"], c["orange"]),
    (a["dainty"], c["yellow"]),
    (a["dainty"], c["gold"]),

    (a["dank"], c["green"]),
    (a["dank"], c["dgreen"]),

    (a["daring"], c["pink"]),
    (a["daring"], c["magenta"]),
    (a["daring"], c["silver"]),
    (a["daring"], c["orange"]),
    (a["daring"], c["brown"]),
    (a["daring"], c["yellow"]),
    (a["daring"], c["black"]),
    (a["daring"], c["red"]),
    (a["daring"], c["white"]),
    (a["daring"], c["cyan"]),
    (a["daring"], c["dgrey"]),
    (a["daring"], c["maroon"]),
    (a["daring"], c["grey"]),
    (a["daring"], c["green"]),
    (a["daring"], c["purple"]),
    (a["daring"], c["lime"]),
    (a["daring"], c["dgreen"]),
    (a["daring"], c["blue"]),
    (a["daring"], c["gold"]),

    (a["dazzling"], c["pink"]),
    (a["dazzling"], c["magenta"]),
    (a["dazzling"], c["silver"]),
    (a["dazzling"], c["orange"]),
    (a["dazzling"], c["yellow"]),
    (a["dazzling"], c["red"]),
    (a["dazzling"], c["white"]),
    (a["dazzling"], c["cyan"]),
    (a["dazzling"], c["green"]),
    (a["dazzling"], c["blue"]),
    (a["dazzling"], c["gold"])
]
    
'''  
    (3, 9), #angelic
    (4, 1), #astonishing
    (4, 2),
    (4, 4),
    (4, 7),
    (4, 15),
    (4, 16),
    (5, 1), #bewildering
    (5, 2),
    (5, 3),
    (5, 4),
    (5, 5),
    (5, 7),
    (5, 8),
    (5, 10),
    (6, 6), #bitter
    (6, 11),
    (6, 13),
    (7, 1), #blush
    (7, 8),
    (8, 1), #bold
    (8, 2),
    (8, 4),
    (8, 16),
    (9, 2), #brash
    (9, 10),
    (9, 16),
    (10, 4), #bright
    (10, 6),
    (10, 8),
    (10, 18),
    (11, 1), #brilliant
    (11, 3),
    (11, 5),
    (11, 7),
    (11, 10),
    (11, 15),
    (11, 18),
    (11, 19),
    (12, 10), #calm
    (13, 18),
    (13, 10), #calming
    (13, 18),
    (14, 1), #charming
    (14, 2),
    (14, 3),
    (14, 4),
    (14, 5),
    (14, 6),
    (14, 7),
    (14, 8),
    (14, 9),
    (14, 10),
    (14, 11),
    (14, 12),
    (14, 13),
    (14, 14),
    (14, 15),
    (14, 16),
    (14, 17),
    (14, 18),
    (14, 19),
    (15, 8), #cheerful
    (16, 18), #chill
    (17, 18), #chilly
    (18, 7), #classic
    (19, 16), #cloudy
    (20, 9), #cold
    (20, 11), 
    (20, 12),
    (21, 1), #confident
    (21, 2),
    (21, 3), 
    (21, 4),
    (21, 5),
    (21, 6),
    (21, 7),
    (21, 8),
    (21, 9),
    (21, 10),
    (21, 11),
    (21, 12),
    (21, 13),
    (21, 14),
    (21, 15),
    (21, 16),
    (21, 17),
    (21, 18),
    (21, 19),
    (22, 1), #cool
    (22, 2),
    (22, 3), 
    (22, 4),
    (22, 5),
    (22, 6),
    (22, 7),
    (22, 8),
    (22, 9),
    (22, 10),
    (22, 11),
    (22, 12),
    (22, 13),
    (22, 14),
    (22, 15),
    (22, 16),
    (22, 17),
    (22, 18),
    (22, 19),
    (23, 7), #cosmic
    (24, 5), #cosy
    (25, 3), #crisp
    (26, 5), #crispy
    (27, 2), #curious
    (27, 4),
    (27, 10),
    (27, 12),
    (27, 15),
    (28, 1), #dainty
    (29, 14), #dank
    (29, 17),
    (30, 1), #daring
    (30, 2), 
    (30, 4),
    (30, 10),
    (30 , 16),
    (31, 7), #dark
    (32, 1) #dazzling
]
'''
