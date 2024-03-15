# colour list (1) pink (2) magenta (3) silver (4) orange (5) brown (6) yellow (7) black (8) red (9) white
# (10) cyan (11) dark grey (12) maroon (13)

from sql.generate.colour.colour_list import colour_list
from sql.generate.language.adjective.adjective_list import adjective_list



a = {adj: index + 1 for index, adj in enumerate(adjective_list)}
c = {color[0]: index+1 for index, color in enumerate(colour_list)}

colour_adjective_list = [
    *( (a["abhorrent"], c[colour]) for colour in ["pink", "magenta", "orange", "brown", "yellow", "black", "red", "white", "cyan", "green", "purple", "lime", "blue"]),

    *( (a["abrasive"], c[colour]) for colour in ["pink", "magenta", "black", "red", "white", "cyan", "grey", "green", "lime", "blue"]),

    *( (a["abysmal"], c[colour]) for colour in ["pink", "magenta", "orange", "brown", "yellow", "black", "red", "white", "cyan", "maroon", "grey", "green", "purple", "lime", "dark green", "blue"]),

    *( (a["active"], c[colour]) for colour in ["pink", "magenta", "silver", "orange", "black", "red", "green", "purple", "lime", "dark green", "blue", "gold"]),

    *( (a["admirable"], c[colour]) for colour in ["pink", "magenta", "silver", "orange", "brown", "yellow", "black", "red", "white", "cyan", "dark grey", "maroon", "grey", "green", "purple", "lime", "dark green", "blue", "gold"]),

    *( (a["advanced"], c[colour]) for colour in ["pink", "magenta", "silver", "orange", "brown", "yellow", "black", "red", "white", "cyan", "dark grey", "maroon", "grey", "green", "purple", "lime", "dark green", "blue", "gold"]),

    *( (a["aerial"], c[colour]) for colour in ["blue"]),

    *( (a["aesthetic"], c[colour]) for colour in ["pink", "magenta", "silver", "orange", "brown", "yellow", "black", "red", "white", "cyan", "dark grey", "maroon", "grey", "green", "purple", "lime", "dark green", "blue", "gold"]),

    *( (a["aggressive"], c[colour]) for colour in ["magenta", "orange", "red", "gold"]),

    *( (a["agreeable"], c[colour]) for colour in ["silver", "black", "dark grey", "maroon", "grey", "dark green", "blue"]),

    *( (a["alluring"], c[colour]) for colour in ["silver", "gold"]),

    *( (a["ambitious"], c[colour]) for colour in ["pink", "magenta", "silver", "orange", "brown", "yellow", "black", "red", "white", "cyan", "dark grey", "maroon", "grey", "green", "purple", "lime", "dark green", "blue", "gold"]),

    *( (a["angelic"], c[colour]) for colour in ["white"]),

    *( (a["amoral"], c[colour]) for colour in ["black", "red", "white", "gold"]),

    *( (a["ancient"], c[colour]) for colour in ["silver", "brown", "yellow", "black", "white", "dark grey", "maroon", "grey", "purple", "dark green", "gold"]),

    *( (a["apocalyptic"], c[colour]) for colour in ["pink", "magenta", "silver", "orange", "brown", "yellow", "black", "red", "white", "cyan", "dark grey", "maroon", "grey", "green", "purple", "lime", "dark green", "blue", "gold"]),

    *( (a["appauling"], c[colour]) for colour in ["pink", "magenta", "orange", "brown", "yellow", "black", "red", "white", "cyan", "dark grey", "grey", "green", "purple", "dark green", "blue"]),

    *( (a["appealing"], c[colour]) for colour in ["pink", "magenta", "silver", "orange", "brown", "yellow", "black", "red", "white", "cyan", "dark grey", "maroon", "grey", "green", "purple", "lime", "dark green", "blue", "gold"]),

    *( (a["apt"], c[colour]) for colour in ["pink", "magenta", "silver", "orange", "brown", "yellow", "black", "red", "white", "cyan", "dark grey", "maroon", "grey", "green", "purple", "lime", "dark green", "blue", "gold"]),

    *( (a["arrogant"], c[colour]) for colour in ["pink", "magenta", "orange", "red", "cyan", "purple", "lime", "gold"]),

    *( (a["astonishing"], c[colour]) for colour in ["pink", "magenta", "silver", "orange", "yellow", "black", "red", "white", "cyan", "purple", "lime", "blue", "gold"]),

    *( (a["attractive"], c[colour]) for colour in ["pink", "magenta", "silver", "orange", "brown", "yellow", "black", "red", "white", "cyan", "dark grey", "maroon", "grey", "green", "purple", "lime", "dark green", "blue", "gold"]),

    *( (a["awesome"], c[colour]) for colour in ["pink", "magenta", "silver", "orange", "brown", "yellow", "black", "red", "white", "cyan", "dark grey", "maroon", "grey", "green", "purple", "lime", "dark green", "blue", "gold"]),

    *( (a["beautiful"], c[colour]) for colour in ["pink", "silver", "brown", "black", "red", "white", "green", "lime", "dark green", "blue", "gold"]),

    *( (a["bewildering"], c[colour]) for colour in ["pink", "magenta", "orange", "brown", "yellow", "black", "red", "cyan", "maroon", "green", "purple", "lime", "dark green", "blue", "gold"]),

    *( (a["bitter"], c[colour]) for colour in ["brown", "yellow", "white", "dark grey", "grey", "lime"]),

    *( (a["blessed"], c[colour]) for colour in ["white"]),

    *( (a["blush"], c[colour]) for colour in ["pink", "red"]),

    *( (a["bold"], c[colour]) for colour in ["pink", "magenta", "orange", "brown", "yellow", "black", "red", "cyan", "maroon", "green", "purple", "lime", "blue", "gold"]),

    *( (a["brash"], c[colour]) for colour in ["magenta", "orange", "brown", "red", "cyan", "purple", "lime", "blue", "gold"]),

    *( (a["brave"], c[colour]) for colour in ["silver", "red", "green", "dark green", "blue", "gold"]),

    *( (a["bright"], c[colour]) for colour in ["pink", "magenta", "silver", "orange", "yellow", "red", "white", "cyan", "green", "purple", "lime", "blue", "gold"]),

    *( (a["brilliant"], c[colour]) for colour in ["pink", "silver", "orange", "brown", "yellow", "black", "red", "white", "green", "purple", "blue", "gold"]),

    *( (a["calm"], c[colour]) for colour in ["blue"]),

    *( (a["calming"], c[colour]) for colour in ["blue"]),

    *( (a["charming"], c[colour]) for colour in ["pink", "magenta", "silver", "orange", "brown", "yellow", "black", "red", "white", "cyan", "dark grey", "maroon", "grey", "green", "purple", "lime", "dark green", "blue", "gold"]),

    *( (a["cheerful"], c[colour]) for colour in ["pink", "magenta", "orange", "yellow", "red", "white", "maroon", "green", "purple", "blue"]),

    *( (a["chill"], c[colour]) for colour in ["silver", "black", "white", "cyan", "lime", "blue"]),

    *( (a["chilly"], c[colour]) for colour in ["silver", "black", "white", "cyan", "lime", "blue"]),

    *( (a["classic"], c[colour]) for colour in ["silver", "black", "red", "white", "blue", "gold"]),

    *( (a["cloudy"], c[colour]) for colour in ["lime", "white"]),

    *( (a["cold"], c[colour]) for colour in ["silver", "black", "white", "cyan", "dark grey", "grey", "blue", "gold"]),
    
    *( (a["confident"], c[colour]) for colour in ["pink", "magenta", "silver", "orange", "brown", "yellow", "black", "red", "white", "cyan", "dark grey", "maroon", "grey", "green", "purple", "lime", "dark green", "blue", "gold"]),

    *( (a["cool"], c[colour]) for colour in ["silver", "yellow", "black", "white", "cyan", "dark grey", "maroon", "grey", "green", "lime", "dark green", "blue", "gold"]),

    *( (a["cooshy"], c[colour]) for colour in ["orange", "brown", "black", "dark grey", "maroon", "grey", "green", "purple", "dark green"]),

    (a["cosmic"], c["black"]),
    
    (a["cosy"], c["brown"]),

    *( (a["courageous"], c[colour]) for colour in ["pink", "magenta", "orange", "red", "green", "purple"]),

    *( (a["crisp"], c[colour]) for colour in ["silver", "white", "lime", "green", "blue", "gold"]),
    
    *( (a["crispy"], c[colour]) for colour in ["brown", "yellow", "gold"]),

    *( (a["curious"], c[colour]) for colour in ["pink", "magenta", "silver", "orange", "brown", "yellow", "black", "red", "white", "cyan", "dark grey", "maroon", "grey", "green", "purple", "lime", "dark green", "blue", "gold"]),

    *( (a["dainty"], c[colour]) for colour in ["pink", "magenta", "silver", "orange", "yellow", "white", "gold"]),

    *( (a["dank"], c[colour]) for colour in ["green", "dark green"]),

    *( (a["daring"], c[colour]) for colour in ["pink", "magenta", "silver", "orange", "brown", "yellow", "black", "red", "white", "cyan", "dark grey", "maroon", "grey", "green", "purple", "lime", "dark green", "blue", "gold"]),

    *( (a["dazzling"], c[colour]) for colour in ["pink", "magenta", "silver", "yellow", "red", "white", "cyan", "purple", "blue", "gold"]),

    *( (a["deep"], c[colour]) for colour in ["magenta", "brown", "black", "green", "purple", "dark green", "blue"]),

    *( (a["delicate"], c[colour]) for colour in ["pink", "silver", "orange", "yellow", "white", "cyan", "dark grey", "maroon", "grey", "green", "dark green"]),

    *( (a["distinctive"], c[colour]) for colour in ["pink", "magenta", "silver", "orange", "brown", "yellow", "black", "red", "white", "cyan", "dark grey", "maroon", "grey", "green", "purple", "lime", "dark green", "blue", "gold"]),

    *( (a["disturbing"], c[colour]) for colour in ["orange", "brown", "yellow", "black", "red", "grey", "green", "purple", "dark green"]),

    *( (a["dramatic"], c[colour]) for colour in ["pink", "magenta", "silver", "orange", "brown", "yellow", "black", "red", "white", "cyan", "dark grey", "maroon", "grey", "green", "purple", "lime", "dark green", "blue", "gold"]),

    *( (a["dreamy"], c[colour]) for colour in ["pink", "magenta", "silver", "black", "white", "dark grey", "maroon", "grey", "green", "purple", "lime", "blue", "gold"]),

    *( (a["earthy"], c[colour]) for colour in ["silver", "gold"]),

    *( (a["elegant"], c[colour]) for colour in ["silver", "gold"]),

    *( (a["enchanting"], c[colour]) for colour in ["silver", "gold"]),

    *( (a["energetic"], c[colour]) for colour in ["pink", "magenta", "silver", "orange", "red", "cyan", "green", "purple", "lime", "blue"]),

    *( (a["expressive"], c[colour]) for colour in ["pink", "magenta", "silver", "orange", "brown", "yellow", "black", "red", "white", "cyan", "dark grey", "maroon", "grey", "green", "purple", "lime", "dark green", "blue", "gold"]),

    *( (a["exquisite"], c[colour]) for colour in ["pink", "magenta", "silver", "orange", "brown", "yellow", "black", "red", "white", "cyan", "dark grey", "maroon", "grey", "green", "purple", "lime", "dark green", "blue", "gold"]),

    *( (a["fancy"], c[colour]) for colour in ["pink", "magenta", "silver", "orange", "black", "white", "cyan", "dark grey", "maroon", "grey", "dark green", "gold"]),

    (a["fierce"], c["red"]),

    (a["fiery"], c["red"]),

    *( (a["fresh"], c[colour]) for colour in ["pink", "orange", "white", "cyan", "green", "lime", "blue"]),

    *( (a["frosty"], c[colour]) for colour in ["silver", "white", "cyan", "blue"]),

    *( (a["funky"], c[colour]) for colour in ["pink", "magenta", "silver", "orange", "brown", "yellow", "black", "red", "white", "cyan", "dark grey", "maroon", "grey", "green", "purple", "lime", "dark green", "blue", "gold"]),

    *( (a["gleaming"], c[colour]) for colour in ["pink", "silver", "white", "gold"]),

    *( (a["glistening"], c[colour]) for colour in ["silver", "white", "gold"]),
 
    *( (a["glorious"], c[colour]) for colour in ["pink", "silver", "black", "red", "white", "cyan", "maroon", "grey", "green", "purple", "lime", "blue", "gold"]),

    *( (a["glossy"], c[colour]) for colour in ["pink", "black", "red", "white", "purple", "lime"]),

    *( (a["glowing"], c[colour]) for colour in ["pink", "silver", "orange", "yellow", "red", "white", "cyan", "green", "purple", "lime", "blue", "gold"]),  

    *( (a["gorgeous"], c[colour]) for colour in ["pink", "magenta", "silver", "orange", "brown", "yellow", "black", "red", "white", "cyan", "dark grey", "maroon", "grey", "green", "purple", "lime", "dark green", "blue", "gold"]),

    *( (a["graceful"], c[colour]) for colour in ["pink", "magenta", "silver", "orange", "brown", "yellow", "black", "red", "white", "cyan", "dark grey", "maroon", "grey", "green", "purple", "lime", "dark green", "blue", "gold"]),

    *( (a["grand"], c[colour]) for colour in ["pink", "silver", "orange", "white", "green", "purple", "lime", "blue", "gold"]),

    *( (a["groovy"], c[colour]) for colour in ["pink", "magenta", "orange", "cyan", "maroon", "green", "purple", "lime", "dark green", "blue"]),

    *( (a["handsome"], c[colour]) for colour in ["pink", "magenta", "silver", "orange", "brown", "yellow", "black", "red", "white", "cyan", "dark grey", "maroon", "grey", "green", "purple", "lime", "dark green", "blue", "gold"]),

    *( (a["haunting"], c[colour]) for colour in ["silver", "black", "white", "dark grey", "maroon", "grey", "dark green"]),

    *( (a["hip"], c[colour]) for colour in ["pink", "magenta", "silver", "orange", "cyan", "maroon", "green", "purple", "lime", "blue"]),

    (a["homely"], c["brown"]),

    (a["hot"], c["pink"]),

    *( (a["icy"], c[colour]) for colour in ["silver", "white", "cyan", "lime", "blue"]),

    *( (a["intense"], c[colour]) for colour in ["pink", "magenta", "orange", "yellow", "red", "cyan", "purple", "lime", "blue", "gold"]),

    *( (a["invigorating"], c[colour]) for colour in ["orange", "red", "cyan", "maroon", "green", "purple", "dark green", "blue", "gold"]),
     
    *( (a["jazzy"], c[colour]) for colour in ["pink", "magenta", "silver", "orange", "brown", "yellow", "black", "red", "dark grey", "maroon", "grey", "green", "purple", "lime", "dark green", "blue", "gold"]),

    *( (a["legendary"], c[colour]) for colour in ["pink", "magenta", "silver", "orange", "brown", "yellow", "black", "red", "white", "cyan", "dark grey", "maroon", "grey", "green", "purple", "lime", "dark green", "blue", "gold"]),

    *( (a["lively"], c[colour]) for colour in ["pink", "magenta", "silver", "orange", "brown", "yellow", "black", "red", "white", "cyan", "dark grey", "maroon", "grey", "green", "purple", "lime", "dark green", "blue", "gold"]),

    *( (a["lovely"], c[colour]) for colour in ["pink", "magenta", "silver", "orange", "brown", "yellow", "black", "red", "white", "cyan", "dark grey", "maroon", "grey", "green", "purple", "lime", "dark green", "blue", "gold"]),

    *( (a["lucky"], c[colour]) for colour in ["pink", "magenta", "silver", "orange", "brown", "yellow", "black", "red", "white", "cyan", "dark grey", "maroon", "grey", "green", "purple", "lime", "dark green", "blue", "gold"]),

    *( (a["lush"], c[colour]) for colour in ["orange", "green", "lime", "dark green"]),

    *( (a["lustrous"], c[colour]) for colour in ["silver", "gold"]),

    *( (a["luxurious"], c[colour]) for colour in ["pink", "magenta", "silver", "orange", "yellow", "black", "red", "white", "cyan", "maroon", "purple", "lime", "gold"]),
  
    *( (a["magnificent"], c[colour]) for colour in ["pink", "magenta", "silver", "orange", "brown", "yellow", "black", "red", "white", "cyan", "dark grey", "maroon", "grey", "green", "purple", "lime", "dark green", "blue", "gold"]),

    *( (a["majestic"], c[colour]) for colour in ["silver", "maroon", "purple", "gold"]),

    *( (a["mellow"], c[colour]) for colour in ["pink", "brown", "yellow", "maroon", "grey", "purple", "lime", "blue", "gold"]),

    *( (a["metallic"], c[colour]) for colour in ["silver", "white", "grey", "blue", "gold"]),

    *( (a["moody"], c[colour]) for colour in ["silver", "brown", "black", "dark grey", "maroon", "grey", "green", "purple", "lime", "dark green", "blue", "gold"]),

    *( (a["mysterious"], c[colour]) for colour in ["pink", "magenta", "silver", "orange", "brown", "yellow", "black", "red", "white", "cyan", "dark grey", "maroon", "grey", "green", "purple", "lime", "dark green", "blue", "gold"]),

    *( (a["mystic"], c[colour]) for colour in ["silver", "grey", "green", "purple", "lime", "dark green", "blue", "gold"]),
    
    (a["natural"], c["green"]),

    *( (a["neat"], c[colour]) for colour in ["pink", "magenta", "silver", "orange", "brown", "yellow", "black", "red", "white", "cyan", "dark grey", "maroon", "grey", "green", "purple", "lime", "dark green", "blue", "gold"]),

    *( (a["nifty"], c[colour]) for colour in ["pink", "magenta", "silver", "orange", "brown", "yellow", "black", "red", "white", "cyan", "dark grey", "maroon", "grey", "green", "purple", "lime", "dark green", "blue", "gold"]),

    *( (a["noble"], c[colour]) for colour in ["silver", "maroon", "purple", "gold"]),

    *( (a["opulent"], c[colour]) for colour in ["silver", "maroon", "purple", "gold"]),

    *( (a["passionate"], c[colour]) for colour in ["pink", "magenta", "orange", "red", "purple", "lime", "blue"]),
    
    (a["pasty"], c["white"]),

    (a["pearly"], c["white"]),

    *( (a["picturesque"], c[colour]) for colour in ["pink", "magenta", "silver", "orange", "brown", "yellow", "black", "red", "white", "cyan", "dark grey", "maroon", "grey", "green", "purple", "lime", "dark green", "blue", "gold"]),

    *( (a["pulchritudinous"], c[colour]) for colour in ["pink", "magenta", "silver", "orange", "brown", "yellow", "black", "red", "white", "cyan", "dark grey", "maroon", "grey", "green", "purple", "lime", "dark green", "blue", "gold"]),

    (a["playful"], c["pink"]),

    (a["plush"], c["pink"]),

    *( (a["poignant"], c[colour]) for colour in ["pink", "magenta", "silver", "orange", "brown", "yellow", "black", "red", "white", "cyan", "dark grey", "maroon", "grey", "green", "purple", "lime", "dark green", "blue", "gold"]),

    *( (a["powerful"], c[colour]) for colour in ["pink", "black", "red", "white", "green", "purple", "blue"]),

    *( (a["pretentious"], c[colour]) for colour in ["pink", "magenta", "silver", "orange", "cyan", "maroon", "grey", "green", "purple", "lime", "blue", "gold"]),
  
    *( (a["pure"], c[colour]) for colour in ["silver", "black", "white", "cyan", "green", "purple", "lime", "blue", "gold"]),

    *( (a["quaint"], c[colour]) for colour in ["pink", "magenta", "silver", "orange", "brown", "yellow", "maroon", "grey", "green", "purple", "lime", "dark green", "blue", "gold"]),

    *( (a["quirky"], c[colour]) for colour in ["pink", "magenta", "silver", "orange", "brown", "yellow", "black", "red", "white", "cyan", "dark grey", "maroon", "grey", "green", "purple", "lime", "dark green", "blue", "gold"]),
    
    *( (a["radiant"], c[colour]) for colour in ["pink", "magenta", "silver", "orange", "yellow", "red", "white", "cyan", "purple", "lime", "blue", "gold"]),

    *( (a["regal"], c[colour]) for colour in ["silver", "maroon", "purple", "gold"]),
    
    *( (a["rich"], c[colour]) for colour in ["orange", "brown", "yellow", "black", "red", "maroon", "grey", "green", "purple", "lime", "dark green", "blue", "gold"]),
 
    (a["ripe"], c["purple"]),
    
    *( (a["romantic"], c[colour]) for colour in ["pink", "red", "gold"]),
    
    *( (a["royal"], c[colour]) for colour in ["silver", "maroon", "purple", "gold"]),

    *( (a["rustic"], c[colour]) for colour in ["brown", "yellow", "red", "dark grey", "maroon", "grey", "green", "purple", "dark green"]),

    *( (a["rusty"], c[colour]) for colour in ["brown", "yellow", "red"]),

    *( (a["serene"], c[colour]) for colour in ["pink", "silver", "black", "white", "cyan", "dark grey", "grey", "green", "blue", "gold"]),

    *( (a["shimmering"], c[colour]) for colour in ["silver", "yellow", "white", "cyan", "blue", "gold"]),

    *( (a["shiny"], c[colour]) for colour in ["pink", "silver", "yellow", "red", "green", "purple", "lime", "blue", "gold"]),

    (a["silky"], c["black"]),
    
    (a["sky"], c["blue"]),

    *( (a["sleek"], c[colour]) for colour in ["silver", "black", "maroon", "grey", "purple", "lime", "dark green", "blue", "gold"]),
    
    *( (a["smart"], c[colour]) for colour in ["silver", "brown", "black", "white", "dark grey", "maroon", "grey", "purple", "dark green", "blue"]),

    (a["snow"], c["white"]),

    *( (a["soft"], c[colour]) for colour in ["pink", "brown", "white", "grey"]),
    
    (a["soily"], c["brown"]),

    (a["sombre"], c["black"]),

    *( (a["soothing"], c[colour]) for colour in ["silver", "brown", "black", "white", "grey", "blue"]),
    
    *( (a["sophisticated"], c[colour]) for colour in ["pink", "magenta", "silver", "orange", "brown", "yellow", "black", "red", "white", "cyan", "dark grey", "maroon", "grey", "green", "purple", "lime", "dark green", "blue", "gold"]),

    *( (a["splendid"], c[colour]) for colour in ["pink", "magenta", "silver", "orange", "brown", "yellow", "black", "red", "white", "cyan", "dark grey", "maroon", "grey", "green", "purple", "lime", "dark green", "blue", "gold"]),

    *( (a["stormy"], c[colour]) for colour in ["black", "white", "dark grey", "grey"]),
    
    *( (a["stylish"], c[colour]) for colour in ["pink", "magenta", "silver", "orange", "brown", "yellow", "black", "red", "white", "cyan", "dark grey", "maroon", "grey", "green", "purple", "lime", "dark green", "blue", "gold"]),

    *( (a["subdued"], c[colour]) for colour in ["silver", "brown", "yellow", "black", "white", "dark grey", "maroon", "grey", "dark green"]),

    *( (a["sublime"], c[colour]) for colour in ["lime", "gold"]),

    *( (a["subtle"], c[colour]) for colour in ["silver", "brown", "yellow", "black", "white", "dark grey", "maroon", "grey", "green", "dark green"]),

    *( (a["sunny"], c[colour]) for colour in ["yellow", "gold"]),

    *( (a["tasteful"], c[colour]) for colour in ["pink", "magenta", "silver", "orange", "brown", "yellow", "black", "red", "white", "cyan", "dark grey", "maroon", "grey", "green", "purple", "lime", "dark green", "blue", "gold"]),

    *( (a["terrific"], c[colour]) for colour in ["pink", "magenta", "silver", "orange", "brown", "yellow", "black", "red", "white", "cyan", "dark grey", "maroon", "grey", "green", "purple", "lime", "dark green", "blue", "gold"]),

    *( (a["timeless"], c[colour]) for colour in ["pink", "magenta", "silver", "orange", "brown", "yellow", "black", "red", "white", "cyan", "dark grey", "maroon", "grey", "green", "purple", "lime", "dark green", "blue", "gold"]),

    *( (a["tranquil"], c[colour]) for colour in ["silver", "black", "white", "dark grey", "maroon", "grey", "green", "dark green", "blue"]),

    *( (a["trusty"], c[colour]) for colour in ["pink", "magenta", "silver", "orange", "brown", "yellow", "black", "red", "white", "cyan", "dark grey", "maroon", "grey", "green", "purple", "lime", "dark green", "blue", "gold"]),

    *( (a["unusual"], c[colour]) for colour in ["magenta", "orange", "cyan", "maroon", "purple", "lime", "gold"]),

    *( (a["velvety"], c[colour]) for colour in ["red", "purple"]),

    *( (a["verdant"], c[colour]) for colour in ["green", "dark green"]),

    *( (a["vibrant"], c[colour]) for colour in ["pink", "yellow", "red", "white", "cyan", "green", "purple", "lime", "blue", "gold"]),

    *( (a["vivid"], c[colour]) for colour in ["pink", "magenta", "orange", "yellow", "red", "white", "cyan", "green", "purple", "lime", "blue", "gold"]),

    *( (a["warm"], c[colour]) for colour in ["orange", "brown", "yellow", "red"]),

    *( (a["watery"], c[colour]) for colour in ["blue", "cyan"]),

    *( (a["whimsical"], c[colour]) for colour in ["pink", "magenta", "silver", "orange", "black", "red", "white", "cyan", "dark grey", "maroon", "grey", "green", "purple", "lime", "dark green", "blue", "gold"]),

    *( (a["wild"], c[colour]) for colour in ["brown", "black", "red", "white", "green", "blue"]),

    *( (a["winter"], c[colour]) for colour in ["silver", "black", "white", "dark grey", "grey", "blue"]),

    *( (a["zany"], c[colour]) for colour in ["pink", "magenta", "silver", "orange", "brown", "yellow", "black", "red", "white", "cyan", "dark grey", "maroon", "grey", "green", "purple", "lime", "dark green", "blue", "gold"])
 ]
