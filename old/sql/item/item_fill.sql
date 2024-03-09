INSERT INTO item_diet(name)
VALUES
    ('none'), --01
    ('meat large'), --02
    ('meat small'),--03
    ('fowl'), --04
    ('vermin'), --05
    ('seafood'), --06
    ('dairy'), --07
    ('plant'), --08
    ('insect'), --09
    ('alcohol'), --10
    ('beverage'), --11
    ('fungus'), --12
    ('mineral'); --13

INSERT INTO item (name, diet, colour, description)
VALUES
    ('wood',             01, 06, 'An old plank of wood.'),
    ('coin',             01, 07, 'An old, rusty coin. Many a person will do many a thing for a bit of coin.'),
    ('wheat',            08, 07, 'A fresh and vibrant crop. Can be baked into breads and brewed into beers.'),
    ('chicken breast',   04, 10, 'Delicious meat of a fowl.'),
    ('bird wings',       04, 02, 'Tasty pieces of fowl meat.'),
    ('fish head',        06, 04, 'An unappetizing brain meal.'),
    ('slime',            05, 15, 'Strange goo.'),
    ('snout',            05, 15, 'Disgusting nose filling.'),
    ('demon heart',      02, 08, 'The heart of a fallen demon. Strange power seems held within.'),
    ('angel heart',      02, 10, 'The heart of a fallen angel. Strange power seems held within.'),
    ('fowl meat',        04, 18, 'The tender meat of a fallen bird.'),
    ('fish fillet',      06, 10, 'A scrumptious meal from the sea.'),
    ('liver',            02, 13, 'A nutritious treat for any adventurer.'),
    ('meat',             02, 09, 'I am not sure what this is but I will try it.'),
    ('bell pepper',      08, 15, 'A crunchy vegetable treat.'),
    ('birds eye pepper', 08, 09, 'A fiery, spicy pepper.'),
    ('ghost pepper',     08, 09, 'A ridiculously spicy pepper.'),
    ('shroom',           12, 10, 'A fungus friend from the forest.'),
    ('sheep head',       02, 10, 'A little gruesome for some but delicious for others.'),
    ('cucumber',         08, 15, 'A refreshing green vegetable.'),
    ('potato',           08, 06, 'A starchy tuber. Delicious in many forms'),
    ('ham',              02, 02, 'Cured and smoked meat.'),
    ('onion',            08, 06, 'A pungent bulb vegetable. Known to make peoplee cry'),
    ('garlic',           08, 10, 'A flavorful, aromatic bulb. Known for having anti-vampiric properties'),
    ('truffle',          12, 10, 'A pungent and fragrant fungus. Known to fetch a high price'),
    ('birds egg',        07, 06, 'An egg from a bird.'),
    ('sausage',          02, 06, 'A seasoned and cured meat.'),
    ('peach',            08, 02, 'A sweet and juicy fruit.'),
    ('watermelon',       08, 18, 'A large, refreshing fruit.'),
    ('mango',            08, 05, 'A tropical and juicy fruit.'),
    ('grapefruit',       08, 05, 'A tangy and citrusy fruit.'),
    ('kiwi',             08, 06, 'A small, fuzzy fruit.'),
    ('lime',             08, 16, 'A sour and citrusy fruit.'),
    ('cherry',           08, 09, 'A sweet and colorful fruit.'),
    ('orange',           08, 05, 'A citrusy and juicy fruit.'),
    ('pear',             08, 15, 'A sweet and crisp fruit.'),
    ('pineapple',        08, 06, 'A tropical and spiky fruit.'),
    ('cockles',          06, 03, 'Edible marine mollusks.'),
    ('mussels',          06, 08, 'Shellfish with a rich flavor.'),
    ('lobster',          06, 09, 'A prized and delicious crustacean.'),
    ('corn',             08, 07, 'A staple grain crop.'),
    ('cranberry',        08, 09, 'A tart and red berry.'),
    ('strawberry',       08, 09, 'A sweet and juicy berry.'),
    ('butter',           07, 07, 'A dairy product made from cream.'),
    ('yeast',            12, 07, 'A microorganism used in fermentation.'),
    ('sugar',            13, 10, 'A sweetening substance.'),
    ('salt',             13, 10, 'A common seasoning.'),
    ('milk',             11, 10, 'A nutritious dairy product.'),
    ('water',            11, 19, 'Pure and essential liquid.'),
    ('cheese',           07, 07, 'A dairy product derived from milk.'),
    ('ginger',           08, 07, 'A pungent and spicy root.'),
    ('spaghetti',        08, 07, 'A delicious pasta dish'),
    ('trunk',            02, 12, 'The trunk of a fallen beast.');
