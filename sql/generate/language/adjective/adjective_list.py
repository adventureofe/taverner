from sql.generate.language.adjective.adjective_connotation.adjective_connotation_list import adjective_connotation_list
ac = {adjective_connotation: index+1 for index, adjective_connotation in enumerate(adjective_connotation_list)}

adjective_list = [
    #for elements
    #alien
    ("alien", ac["neutral"]),
    ("otherworldly", ac["neutral"]),
    ("extraterrestrial", ac["neutral"]),
    #air,
    ("airy", ac["neutral"]),
    ("windy", ac["neutral"]),
    ("gusty", ac["neutral"]),
    #chaos,
    ("chaotic", ac["neutral"]),
    ("mindboggling", ac["neutral"]),
    #electricity,
    ("electrifying", ac["neutral"]),
    ("shocking", ac["neutral"]),
    #evil,
    ("evil", ac["neutral"]),
    ("devilish", ac["neutral"]),
    ("demonic", ac["neutral"]),
    #fire,
    ("fiery", ac["neutral"]),
    ("flaming", ac["neutral"]),
    ("flamin", ac["neutral"]),
    ("burning", ac["neutral"]),
    #holiness,
    ("holy", ac["neutral"]),
    ("heavenly", ac["neutral"]),
    #ice,
    ("icy", ac["neutral"]),
    ("freezing", ac["neutral"]),
    ("freezin", ac["neutral"]),
    ("chilling", ac["neutral"]),
    ("chillin", ac["neutral"]),
    #metal,
    ("metal", ac["neutral"]),
    ("metallic", ac["neutral"]),
    #normal,
    ("normal", ac["neutral"]),
    ("magicless", ac["neutral"]),
    #plant,
    ("planty", ac["neutral"]),
    ("leafy", ac["neutral"]),
    ("veggie", ac["neutral"]),
    ("veggy", ac["neutral"]),
    #poison,
    ("poison", ac["neutral"]),
    ("poisonous", ac["neutral"]),
    ("toxic", ac["neutral"]),
    #radiation,
    ("radioactive", ac["neutral"]),
    ("atomic", ac["neutral"]),
    #undead,
    ("undead", ac["neutral"]),
    ("zombie", ac["neutral"]),
    #water,
    ("watery", ac["neutral"]),
    ("wet", ac["neutral"]),
    #fungus
    ("fungal", ac["neutral"]),
    ("mushroomy", ac["neutral"]),

    #general entries
    ("abhorrent", ac["hatred"]),
    ("abrasive", ac["extremely negative"]),
    ("abysmal", ac["hatred"]),
    ("active", ac["slightly positive"]),
    ("admirable", ac["extremely positive"]),
    ("advanced", ac["extremely positive"]),
    ("aerial", ac["neutral"]), 
    ("aesthetic", ac["extremely positive"]), 
    ("aggressive", ac["slightly negative"]),
    ("agreeable", ac["slightly positive"]),
    ("alluring", ac["seductive"]),
    ("ambitious", ac["slightly positive"]),
    ("amoral", ac["slightly negative"]),
    ("ancient", ac["neutral"]),
    ("angelic", ac["extremely positive"]),
    ("apocalyptic", ac["extremely negative"]),
    ("appauling", ac["extremely negative"]),
    ("appealing", ac["slightly positive"]),
    ("apt", ac["slightly positive"]),
    ("arrogant", ac["slightly negative"]),
    ("astonishing", ac["extremely positive"]), 
    ("attractive", ac["seductive"]),
    ("awesome", ac["extremely positive"]),
    ("beautiful", ac["seductive"]),
    ("bewildering", ac["perplexing"]), 
    ("bitter", ac["slightly negative"]),
    ("blessed", ac["extremely positive"]),
    ("blush", ac["neutral"]), 
    ("bold", ac["slightly negative"]), 
    ("brash", ac["slightly negative"]), 
    ("brave", ac["extremely positive"]),
    ("bright", ac["slightly positive"]), 
    ("brilliant", ac["extremely positive"]),
    ("calm", ac["slightly positive"]), 
    ("calming", ac["slightly positive"]), 
    ("charming", ac["seductive"]), 
    ("cheerful", ac["extremely positive"]),
    ("chill", ac["slightly positive"]), 
    ("chilly", ac["slightly negative"]), 
    ("classic", ac["slightly positive"]),
    ("cloudy", ac["slightly negative"]), 
    ("cold", ac["slightly negative"]), 
    ("confident", ac["extremely positive"]),
    ("confusing", ac["perplexing"]),
    ("cool", ac["extremely positive"]), 
    ("cooshy", ac["slightly negative"]),
    ("cosmic", ac["slightly positive"]), 
    ("cosy", ac["extremely positive"]), 
    ("courageous", ac["extremely positive"]),
    ("crisp", ac["slightly positive"]), 
    ("crispy", ac["slightly positive"]),
    ("curious", ac["neutral"]), 
    ("dainty", ac["slightly positive"]), 
    ("dank", ac["extremely positive"]), 
    ("daring", ac["slightly positive"]), 
    ("dazzling", ac["extremely positive"]), 
    ("deep", ac["slightly positive"]), 
    ("delicate", ac["slightly positive"]), 
    ("distinctive", ac["slightly positive"]), 
    ("disturbing", ac["extremely negative"]), #up to here is filled into colour adjecti, ac[""]ve
    ("drab", ac["slightly negative"]),
    ("dramatic", ac["neutral"]), 
    ("dreamy", ac["seductive"]), 
    ("earthy", ac["neutral"]), 
    ("easy", ac["slightly positive"]),
    ("elder", ac["neutral"]),
    ("elegant", ac["extremely positive"]), 
    ("enchanting", ac["extremely positive"]), 
    ("energetic", ac["extremely positive"]), 
    ("evil", ac["hatred"]),
    ("exciting", ac["extremely positive"]),
    ("expensive", ac["slightly negative"]),
    ("expressive", ac["neutral"]), 
    ("exquisite", ac["extremely positive"]), 
    ("faithful", ac["slightly positive"]),
    ("famous", ac["slightly positive"]),
    ("fancy", ac["seductive"]), 
    ("fat", ac["slightly negative"]),
    ("fierce", ac["slightly negative"]), 
    ("fiery", ac["neutral"]), 
    ("fresh", ac["slightly positive"]), 
    ("frosty", ac["slightly negative"]), 
    ("funky", ac["extremely positive"]), 
    ("gentle", ac["slightly positive"]),
    ("glamorous", ac["extremely positive"]),
    ("gleaming", ac["extremely positive"]), 
    ("glistening", ac["neutral"]), 
    ("glorious", ac["extremely positive"]), 
    ("glossy", ac["neutral"]), 
    ("glowing", ac["slightly positive"]),
    ("good", ac["slightly positive"]),
    ("gorgeous", ac["seductive"]),
    ("graceful", ac["extremely positive"]), 
    ("grand", ac["extremely positive"]), 
    ("groovy", ac["extremely positive"]),
    ("handsome", ac["seductive"]),
    ("happy", ac["extremely positive"]),
    ("haunting", ac["extremely negative"]), 
    ("hip", ac["slightly positive"]), 
    ("homely", ac["slightly positive"]),
    ("hot", ac["seductive"]),
    ("icy", ac["slightly negative"]), 
    ("important", ac["neutral"]),
    ("intense", ac["neutral"]), 
    ("interesting", ac["slightly positive"]),
    ("invigorating", ac["extremely positive"]), 
    ("jazzy", ac["slightly positive"]), 
    ("jolly", ac["slightly positive"]),
    ("journied", ac["neutral"]),
    ("joyful", ac["slightly positive"]),
    ("legendary", ac["extremely positive"]), 
    ("lively", ac["slightly positive"]), 
    ("lovely", ac["seductive"]),
    ("lucky", ac["extremely positive"]),
    ("lush", ac["slightly positive"]),
    ("lustrous", ac["slightly positive"]),
    ("luxurious", ac["extremely positive"]), 
    ("magnificent", ac["extremely positive"]),
    ("majestic", ac["extremely positive"]), 
    ("mellow", ac["slightly positive"]), 
    ("metallic", ac["neutral"]), 
    ("moody", ac["slightly negative"]), 
    ("moral", ac["slightly positive"]),
    ("mushy", ac["slightly negative"]),
    ("mysterious", ac["slightly positive"]),
    ("mystic", ac["extremely positive"]), 
    ("natural", ac["neutral"]), 
    ("neat", ac["slightly positive"]), 
    ("nifty", ac["extremely positive"]), 
    ("noble", ac["slightly positive"]), 
    ("old", ac["neutral"]),
    ("opulent", ac["slightly negative"]), 
    ("passionate", ac["slightly positive"]), 
    ("pasty", ac["slightly negative"]), 
    ("pearly", ac["slightly positive"]), 
    ("phat", ac["extremely positive"]),
    ("picturesque", ac["extremely positive"]),
    ("pitiful", ac["extremely negative"]),
    ("playful", ac["slightly positive"]), 
    ("plump", ac["neutral"]),
    ("plush", ac["slightly positive"]), 
    ("poignant", ac["slightly negative"]), 
    ("polite", ac["slightly positive"]),
    ("powerful", ac["slightly positive"]), 
    ("pretentious", ac["slightly negative"]), 
    ("proud", ac["slightly positive"]),
    ("pulchritudinous", ac["seductive"]),
    ("pure", ac["slightly positive"]), 
    ("quaint", ac["slightly positive"]), 
    ("quiet", ac["neutral"]),
    ("quirky", ac["slightly positive"]), 
    ("radiant", ac["slightly positive"]), 
    ("regal", ac["slightly positive"]), 
    ("rich", ac["slightly positive"]), 
    ("ripe", ac["slightly positive"]), 
    ("romantic", ac["seductive"]), 
    ("royal", ac["slightly positive"]), 
    ("rustic", ac["slightly positive"]), 
    ("rusty", ac["slightly negative"]), 
    ("scruffy", ac["slightly negative"]),
    ("serene", ac["extremely positive"]), 
    ("shapely", ac["seductive"]),
    ("shimmering", ac["neutral"]), 
    ("shiny", ac["neutral"]), 
    ("shy", ac["slightly negative"]),
    ("silky", ac["neutral"]), 
    ("silly", ac["slightly negative"]),
    ("sky", ac["slightly positive"]), 
    ("sleek", ac["slightly positive"]), 
    ("smart", ac["slightly positive"]), 
    ("snow", ac["neutral"]), 
    ("soft", ac["neutral"]), 
    ("soily", ac["slightly negative"]), 
    ("sombre", ac["slightly negative"]), 
    ("soothing", ac["slightly positive"]), 
    ("sophisticated", ac["slightly positive"]), 
    ("splendid", ac["extremely positive"]),
    ("stocky", ac["neutral"]),
    ("stormy", ac["slightly negative"]), 
    ("stylish", ac["slightly positive"]), 
    ("subdued", ac["neutral"]), 
    ("sublime", ac["extremely positive"]), 
    ("subtle", ac["neutral"]), 
    ("sunny", ac["slightly positive"]), 
    ("tasteful", ac["extremely positive"]), 
    ("terrific", ac["extremely positive"]), 
    ("timeless", ac["extremely positive"]), 
    ("tranquil", ac["slightly positive"]), 
    ("trusty", ac["extremely positive"]), 
    ("unimportant", ac["slightly negative"]),
    ("uninteresting", ac["extremely negative"]),
    ("unkempt", ac["slightly negative"]),
    ("unslightly", ac["extremely negative"]),
    ("unusual", ac["perplexing"]), 
    ("uptight", ac["slightly negative"]),
    ("vast", ac["neutral"]),
    ("velvety", ac["slightly positive"]), 
    ("verdant", ac["slightly positive"]), 
    ("vibrant", ac["slightly positive"]), 
    ("vivid", ac["extremely positive"]), 
    ("warm", ac["slightly positive"]), 
    ("watery", ac["slightly negative"]), 
    ("whimsical", ac["extremely positive"]), 
    ("wild", ac["neutral"]), 
    ("winter", ac["slightly negative"]), 
    ("wonderful", ac["extremely positive"]),
    ("zany", ac["slightly negative"]),
    ("zealous", ac["neutral"]),
    ("stalky", ac["neutral"])
]
