import sys
import sqlite3
import pandas as pd

from sql.generate.colour.colour_list import colour_list

from sql.generate.item.item_diet.item_diet_list import item_diet_list

from sql.generate.language.name.person_name.person_name_gender.person_name_gender_list import person_name_gender_list

from sql.generate.language.name.person_name.person_name_category.person_name_category_list import person_name_category_list


ng = {person_name_gender: index+1 for index, person_name_gender in enumerate(person_name_gender_list)}

nc = {person_name_category: index+1 for index, person_name_category in enumerate(person_name_category_list)}


person_name_list = [
    #genderless a
    ("acorn", ng["genderless"], nc["comical"]),  
    ("apricot", ng["genderless"], nc["comical"]),  
    ("applejack", ng["genderless"], nc["comical"]),  
    ("alex", ng["genderless"], nc["english"]),
    ("andromeda", ng["genderless"], nc["ancient"]),
    ("ash", ng["genderless"], nc["english"]),
    #genderless b
    ("beany", ng["genderless"], nc["comical"]),
    ("beanie", ng["genderless"], nc["comical"]),
    ("beans", ng["genderless"], nc["comical"]),
    ("biscuit", ng["genderless"], nc["comical"]),
    ("biscuits", ng["genderless"], nc["comical"]),
    ("butters", ng["genderless"], nc["comical"]), 
    ("bo", ng["genderless"], nc["english"]),
    ("boo", ng["genderless"], nc["comical"]),
    ("bootsy", ng["genderless"], nc["comical"]),
    ("breadstick", ng["genderless"], nc["comical"]),
    ("breadsticks", ng["genderless"], nc["comical"]),
    ("bubsy", ng["genderless"], nc["comical"]),
    ("bugsy", ng["genderless"], nc["comical"]),
    ("butch", ng["genderless"], nc["english"]),
    ("button", ng["genderless"], nc["comical"]),
    ("bubble", ng["genderless"], nc["comical"]),
    ("bubbles", ng["genderless"], nc["comical"]),
    ("buttons", ng["genderless"], nc["comical"]),
    ("binky", ng["genderless"], nc["comical"]),
    ("butterscotch", ng["genderless"], nc["comical"]),
    #genderless c
    ("cookie", ng["genderless"], nc["comical"]),
    ("cookies", ng["genderless"], nc["comical"]),
    ("cheddar", ng["genderless"], nc["comical"]),
    ("cheese", ng["genderless"], nc["comical"]),
    ("cheesy", ng["genderless"], nc["comical"]),
    ("chubs", ng["genderless"], nc["comical"]),
    ("chip", ng["genderless"], nc["comical"]),
    ("chippa", ng["genderless"], nc["comical"]),
    ("chipper", ng["genderless"], nc["comical"]),
    ("chunky", ng["genderless"], nc["comical"]),
    ("chunkie", ng["genderless"], nc["comical"]),
    ("checkers", ng["genderless"], nc["comical"]),
    ("cupcake", ng["genderless"], nc["comical"]),
    ("cutie", ng["genderless"], nc["comical"]),
    ("charm", ng["genderless"], nc["comical"]),
    #genderless d
    ("dash", ng["genderless"], nc["comical"]),
    ("dashy", ng["genderless"], nc["comical"]),
    ("dylan", ng["genderless"], nc["english"]),
    ("dimples", ng["genderless"], nc["comical"]),
    ("dewdrop", ng["genderless"], nc["comical"]),
    ("dinky", ng["genderless"], nc["comical"]),
    ("doodlebug", ng["genderless"], nc["comical"]),
    #genderless e
    ("egg", ng["genderless"], nc["comical"]),
    ("eggy", ng["genderless"], nc["comical"]),
    ("eggie", ng["genderless"], nc["comical"]),
    ("echo", ng["genderless"], nc["english"]),
    ("eclipse", ng["genderless"], nc["english"]),
    ("excalibur", ng["genderless"], nc["comical"]),
    ("espresso", ng["genderless"], nc["mediteranean"]),
    # male names a
    ("aaron", ng["male"], nc["irish"]),
    ("abdo", ng["male"], nc["arabic"]),
    ("abdul", ng["male"], nc["arabic"]),
    ("abdullah", ng["male"], nc["arabic"]),
    ("abe", ng["male"], nc["ancient"]),
    ("abel", ng["male"], nc["ancient"]),
    ("abraham", ng["male"], nc["ancient"]),
    ("ace", ng["male"], nc["comical"]),
    ("achilles", ng["male"], nc["ancient"]),
    ("adam", ng["male"], nc["english"]),
    ("adrian", ng["male"], nc["english"]),
    ("aidan", ng["male"], nc["irish"]),
    ("ainsley", ng["male"], nc["english"]),
    ("al", ng["male"], nc["english"]),
    ("aladin", ng["male"], nc["arabic"]),
    ("alan", ng["male"], nc["english"]),
    ("albert", ng["male"], nc["english"]),
    ("alberto", ng["male"], nc["mediteranean"]),
    ("aljandro", ng["male"], nc["mediteranean"]),
    ("alexander", ng["male"], nc["english"]),
    ("alfie", ng["male"], nc["english"]),
    ("alfonso", ng["male"], nc["mediteranean"]),
    ("alfred", ng["male"], nc["english"]),
    ("ali", ng["male"], nc["arabic"]),
    ("alistair", ng["male"], nc["english"]),
    ("allister", ng["male"], nc["english"]),
    ("alonzo", ng["male"], nc["mediteranean"]),
    ("alucard", ng["male"], nc["comical"]),
    ("alvin", ng["male"], nc["english"]),
    ("amadeus", ng["male"], nc["ancient"]),
    ("asmodeus", ng["male"], nc["ancient"]),
    ("amos", ng["male"], nc["english"]),
    ("anakin", ng["male"], nc["comical"]),
    ("anders", ng["male"], nc["norse"]),
    ("andre", ng["male"], nc["mediteranean"]),
    ("andrew", ng["male"], nc["english"]),
    ("andy", ng["male"], nc["english"]),
    ("angus", ng["male"], nc["scottish"]),
    ("ant", ng["male"], nc["english"]),
    ("anthony", ng["male"], nc["english"]),
    ("antonio", ng["male"], nc["mediteranean"]),
    ("aphex", ng["male"], nc["comical"]),
    ("apu", ng["male"], nc["comical"]),
    ("apollo", ng["male"], nc["ancient"]),
    ("archibald", ng["male"], nc["english"]),
    ("archie", ng["male"], nc["english"]),
    ("archimedes", ng["male"], nc["ancient"]),
    ("aristotle", ng["male"], nc["ancient"]),
    ("arnie", ng["male"], nc["english"]),
    ("arno", ng["male"], nc["irish"]),
    ("arnold", ng["male"], nc["english"]),
    ("arthur", ng["male"], nc["english"]),
    ("artie", ng["male"], nc["english"]),
    ("aston", ng["male"], nc["english"]),
    ("atilla", ng["male"], nc["ancient"]),
    ("augustus", ng["male"], nc["ancient"]),
    ("austin", ng["male"], nc["english"]),
    ("axel", ng["male"], nc["german"]),
    ("azriel", ng["male"], nc["ancient"]),
    ("ahmed", ng["male"], nc["arabic"]),
    #male names b
    ("balthazar", ng["male"], nc["ancient"]),
    ("bane", ng["male"], nc["comical"]),
    ("baptiste", ng["male"], nc["ancient"]),
    ("basil", ng["male"], nc["comical"]),
    ("banjo", ng["male"], nc["comical"]),
    ("barrack", ng["male"], nc["english"]),
    ("barack", ng["male"], nc["english"]),
    ("barnabas", ng["male"], nc["ancient"]),
    ("barnaby", ng["male"], nc["english"]),
    ("barney", ng["male"], nc["english"]),
    ("barry", ng["male"], nc["english"]),
    ("bart", ng["male"], nc["comical"]),
    ("bartholomew", ng["male"], nc["ancient"]),
    ("baxter", ng["male"], nc["english"]),
    ("baz", ng["male"], nc["comical"]),
    ("ben", ng["male"], nc["english"]),
    ("benedict", ng["male"], nc["english"]),
    ("benito", ng["male"], nc["mediteranean"]),
    ("benjamin", ng["male"], nc["english"]),
    ("benjy", ng["male"], nc["english"]),
    ("benny", ng["male"], nc["english"]),
    ("bentley", ng["male"], nc["english"]),
    ("bernard", ng["male"], nc["english"]),
    ("bernardo", ng["male"], nc["mediteranean"]),
    ("bernie", ng["male"], nc["comical"]),
    ("biggy", ng["male"], nc["comical"]),
    ("billy", ng["male"], nc["english"]),
    ("bjorn", ng["male"], nc["norse"]),
    ("blaine", ng["male"], nc["english"]),
    ("blaze", ng["male"], nc["comical"]),
    ("bob", ng["male"], nc["english"]),
    ("bobby", ng["male"], nc["english"]),
    ("boberto", ng["male"], nc["comical"]),
    ("boris", ng["male"], nc["german"]),
    ("bosco", ng["male"], nc["comical"]),
    ("boswell", ng["male"], nc["english"]),
    ("brad", ng["male"], nc["english"]),
    ("bradley", ng["male"], nc["english"]),
    ("bram", ng["male"], nc["german"]),
    ("brandon", ng["male"], nc["english"]),
    ("brawly", ng["male"], nc["comical"]),
    ("brendan", ng["male"], nc["english"]),
    ("brett", ng["male"], nc["english"]),
    ("brian", ng["male"], nc["english"]),
    ("brain", ng["male"], nc["comical"]),
    ("brock", ng["male"], nc["english"]),
    ("broderick", ng["male"], nc["scottish"]),
    ("bruce", ng["male"], nc["scottish"]),
    ("bruno", ng["male"], nc["mediteranean"]),
    ("bryce", ng["male"], nc["english"]),
    ("bubba", ng["male"], nc["comical"]),
    ("buck", ng["male"], nc["english"]),
    ("buddha", ng["male"], nc["comical"]),
    ("buddy", ng["male"], nc["english"]),
    ("buster", ng["male"], nc["english"]),
    ("buxley", ng["male"], nc["english"]),
    ("buzz", ng["male"], nc["comical"]),
    ("byron", ng["male"], nc["english"]),
    ("beethoven", ng["male"], nc["ancient"]),
    #female names a
    ("abbie", ng["female"], nc["english"]),
    ("abigail", ng["female"], nc["english"]),
    ("addison", ng["female"], nc["english"]),
    ("adele", ng["female"], nc["english"]),
    ("adelaide", ng["female"], nc["english"]),
    ("adeline", ng["female"], nc["english"]),
    ("adrianna", ng["female"], nc["mediteranean"]),
    ("agatha", ng["female"], nc["english"]),
    ("agnes", ng["female"], nc["scottish"]),
    ("aileen", ng["female"], nc["english"]),
    ("alanis", ng["female"], nc["english"]),
    ("alannah", ng["female"], nc["english"]),
    ("almond", ng["female"], nc["comical"]),
    ("alberta", ng["female"], nc["mediteranean"]),
    ("alesha", ng["female"], nc["english"]),
    ("alexa", ng["female"], nc["english"]),
    ("alexandra", ng["female"], nc["mediteranean"]),
    ("alexis", ng["female"], nc["english"]),
    ("alice", ng["female"], nc["english"]),
    ("alicia", ng["female"], nc["mediteranean"]),
    ("allison", ng["female"], nc["english"]),
    ("amanda", ng["female"], nc["english"]),
    ("amber", ng["female"], nc["english"]),
    ("amelia", ng["female"], nc["mediteranean"]),
    ("amira", ng["female"], nc["arabic"]),
    ("amy", ng["female"], nc["english"]),
    ("anabel", ng["female"], nc["english"]),
    ("anastasia", ng["female"], nc["mediteranean"]),
    ("angela", ng["female"], nc["english"]),
    ("angelina", ng["female"], nc["mediteranean"]),
    ("angelica", ng["female"], nc["english"]),
    ("anna", ng["female"], nc["english"]),
    ("annabelle", ng["female"], nc["english"]),
    ("anne", ng["female"], nc["english"]),
    ("arabelle", ng["female"], nc["arabic"]),
    ("ariana", ng["female"], nc["mediteranean"]),
    ("ariel", ng["female"], nc["english"]),
    ("arrabella", ng["female"], nc["arabic"]),
    ("artemis", ng["female"], nc["ancient"]),
    ("aryana", ng["female"], nc["mediteranean"]),
    ("ashley", ng["female"], nc["english"]),
    ("athena", ng["female"], nc["ancient"]),
    ("audrey", ng["female"], nc["english"]),
    ("autumn", ng["female"], nc["english"]),
    ("ava", ng["female"], nc["english"]),
    ("aoife", ng["female"], nc["irish"]),
    #female names b
    ("babs", ng["female"], nc["comical"]),
    ("bailey", ng["female"], nc["english"]),
    ("barbara", ng["female"], nc["english"]),
    ("bea", ng["female"], nc["english"]),
    ("beatrice", ng["female"], nc["english"]),
    ("beatrix", ng["female"], nc["english"]),
    ("becca", ng["female"], nc["english"]),
    ("becky", ng["female"], nc["english"]),
    ("belinda", ng["female"], nc["english"]),
    ("belle", ng["female"], nc["english"]),
    ("bernadette", ng["female"], nc["scottish"]),
    ("bertha", ng["female"], nc["english"]),
    ("bessie", ng["female"], nc["english"]),
    ("beth", ng["female"], nc["english"]),
    ("bethany", ng["female"], nc["english"]),
    ("betsy", ng["female"], nc["english"]),
    ("betty", ng["female"], nc["english"]),
    ("beverly", ng["female"], nc["english"]),
    ("beyonce", ng["female"], nc["comical"]),
    ("bianca", ng["female"], nc["english"]),
    ("billie", ng["female"], nc["english"]),
    ("blanche", ng["female"], nc["english"]),
    ("blossom", ng["female"], nc["english"]),
    ("blythe", ng["female"], nc["english"]),
    ("bonnie", ng["female"], nc["english"]),
    ("brandy", ng["female"], nc["english"]),
    ("bree", ng["female"], nc["english"]),
    ("brenda", ng["female"], nc["english"]),
    ("bridget", ng["female"], nc["irish"]),
    ("brigette", ng["female"], nc["irish"]),
    ("brie", ng["female"], nc["english"]),
    ("britney", ng["female"], nc["english"]),
    ("brooke", ng["female"], nc["english"]),
    ("buffy", ng["female"], nc["comical"]),
    ("buttercup", ng["female"], nc["comical"]),
    ]
'''
    #male names b
    ('Balthazar',   2, 5),
    ('Bane',        2, 5),
    ('Baptiste',    2, 3),
    ('Basil',       2, 5),
    ('Banjo',       2, 5),
    ('Barack',      2, 3),
    ('Barnabas',    2, 4),
    ('Barnaby',     2, 5),
    ('Barney',      2, 2),
    ('Barry',       2, 2),
    ('Bart',        2, 2),
    ('Bartholomew', 2, 4),
    ('Basil',       2, 2),
    ('Baxter',      2, 2),
    ('Baz',         2, 2),
    ('Ben',         2, 2),
    ('Benedict',    2, 3),
    ('Benito',      2, 2),
    ('Benjamin',    2, 2),
    ('Benjy',       2, 5),
    ('Benny',       2, 2),
    ('Bentley',     2, 4),
    ('Bernard',     2, 2),
    ('Bernie',      2, 2),
    ('Biggy',       2, 5),
    ('Billy',       2, 2),
    ('Bjorn',       2, 3),
    ('Blaine',      2, 2),
    ('Blaze',       2, 2),
    ('Bob',         2, 2),
    ('Bobby',       2, 2),
    ('Boris',       2, 2),
    ('Bosco',       2, 5),
    ('Boswell',     2, 4),
    ('Brad',        2, 2),
    ('Bradley',     2, 2),
    ('Bram',        2, 3),
    ('Brandon',     2, 2),
    ('Brawly',      2, 5),
    ('Brendan',     2, 2),
    ('Brett',       2, 2),
    ('Brian',       2, 2),
    ('Brock',       2, 2),
    ('Broderick',   2, 4),
    ('Bruce',       2, 2),
    ('Bruno',       2, 3),
    ('Bryce',       2, 2),
    ('Brycen',      2, 2),
    ('Bubba',       2, 5),
    ('Buck',        2, 2),
    ('Bucky',       2, 2),
    ('Buddha',      2, 5),
    ('Buddy',       2, 2),
    ('Buster',      2, 2),
    ('Butters',     2, 5),
    ('Buxley',      2, 4),
    ('Buzz',        2, 2),
    ('Byron',       2, 2),
    ('Beethoven',   2, 5),
--male names c
    ('Caesar',      2, 3),
    ('Cain',        2, 4),
    ('Cairo',       2, 4),
    ('Callum',      2, 2),
    ('Calvin',      2, 2),
    ('Camden',      2, 2),
    ('Cameron',     2, 2),
    ('Carl',        2, 2),
    ('Carter',      2, 2),
    ('Cassius',     2, 4),
    ('Cecil',       2, 4),
    ('Cedric',      2, 4),
    ('Chad',        2, 2),
    ('Chadwick',    2, 4),
    ('Chance',      2, 5),
    ('Chandler',    2, 2),
    ('Chester',     2, 2),
    ('Chris',       2, 2),
    ('Christian',   2, 2),
    ('Christopher', 2, 2),
    ('Clarence',    2, 4),
    ('Clark',       2, 2),
    ('Claude',      2, 2),
    ('Cleveland',   2, 3),
    ('Clive',       2, 2),
    ('Connor',      2, 3),
    ('Conor',       2, 3),
    ('Constantine', 2, 4),
    ('Cormac',      2, 3),
    ('Craig',       2, 2),
    ('Cristiano',   2, 3),
    ('Curtis',      2, 4),
    ('Cyril',       2, 3),
    ('Cyrus',       2, 2),
    ('Chico',       2, 5),
    ('Chopper',     2, 5),
    ('Charles',     2, 4),
    ('Clifford',    2, 4),
    ('Crash',       2, 5),
    ('Coach',       2, 5),
    ('Cheech',      2, 5),
    ('Chong',       2, 5),
    ('Cliff',       2, 2),
    ('Cormac', 2, 3),
    ('Carlos', 2, 3),
    ('Crash', 2, 5),
--male names D
    ('Dan',         2, 2),
    ('Danny',       2, 2),
    ('Daniel',      2, 2),
    ('David',       2, 2),
    ('Dave',        2, 2),
    ('Dylan',       2, 2),
    ('Dyl',         2, 2),
    ('Dominic',     2, 2),
    ('Dom',         2, 2),
    ('Darius',      2, 3),
    ('Declan',      2, 2),
    ('Decky',       2, 5),
    ('Damian',      2, 2),
    ('Diego',       2, 3),
    ('Dean',        2, 2),
    ('Dante',       2, 5),
    ('Digby',       2, 5),
    ('Dudley',      2, 4),
    ('Derick',      2, 4),
    ('Dwanye',      2, 5),
    ('Douglas',     2, 2),
    ('Doug',        2, 2),
    ('Drake',       2, 2),
    ('Drew',        2, 2),
    ('Dennis',      2, 2),
    ('Dustin',      2, 2),
    ('Donald',      2, 2),
    ('Donny',       2, 2),
    ('Don',         2, 2),
    ('Dmitri',      2, 4),
    ('Dick',        2, 5),
    ('DJ',          2, 5),
    ('Dodge',       2, 5),
    ('Duke',        2, 2),
    ('Dmitry', 2, 3),
--male names E
    ('Earl',        2, 2),
    ('Edd',         2, 2),
    ('Eddie',       2, 2),
    ('Eddy',        2, 2),
    ('Edgar',       2, 2),
    ('Edward',      2, 2),
    ('Edwin',       2, 4),
    ('Eithan',      2, 2),
    ('Eli',         2, 4),
    ('Elijah',      2, 2),
    ('Elliot',      2, 2),
    ('Emiliano',    2, 3),
    ('Emilio',      2, 3),
    ('Emmanuel',    2, 3),
    ('Enzo',        2, 3),
    ('Eric',        2, 2),
    ('Escobar',     2, 5),
    ('Estaban',     2, 3),
    ('Ethan',       2, 2),
    ('Evan',        2, 2),
    ('Evan',        2, 2),
    ('Ezra',        2, 3),
    ('Enoch',       2, 4),
    ('Elmer',       2, 4),
    ('Elon',        2, 5),
    ('Eugene',      2, 2),
    ('Earnest',     2, 2),
    ('Elvis',       2, 5),
    ('Eduardo',     2, 3),
    ('Eamon', 2, 3),
--female names A
    ('Abbie',       3, 2),
    ('Abigail',     3, 2),
    ('Addison',     3, 2),
    ('Adele',       3, 5),
    ('Adelaide',    3, 4),
    ('Adeline',     3, 2),
    ('Adrianna',    3, 2),
    ('Agatha',      3, 4),
    ('Agnes',       3, 4),
    ('Aileen',      3, 2),
    ('Alanis',      3, 2),
    ('Alannah',     3, 2),
    ('Almond',      3, 5),
    ('Alberta',     3, 2),
    ('Alesha',      3, 5),
    ('Alexa',       3, 5),
    ('Alexandra',   3, 2),
    ('Alexis',      3, 2),
    ('Alice',       3, 2),
    ('Alicia',      3, 2),
    ('Allison',     3, 2),
    ('Amanda',      3, 2),
    ('Amber',       3, 2),
    ('Amelia',      3, 2),
    ('Amira',       3, 3),
    ('Amy',         3, 2),
    ('Anabell',     3, 2),
    ('Anastasia',   3, 5),
    ('Angela',      3, 2),
    ('Angelina',    3, 2),
    ('Angelica',    3, 2),
    ('Anna',        3, 2),
    ('Annabelle',   3, 2),
    ('Anne',        3, 2),
    ('Arabelle',    3, 2),
    ('Ariana',      3, 2),
    ('Ariel',       3, 2),
    ('Arrabella',   3, 2),
    ('Artemis',     3, 4),
    ('Aryana',      3, 2),
    ('Ashley',      3, 2),
    ('Athena',      3, 4),
    ('Audrey',      3, 2),
    ('Autumn',      3, 2),
    ('Ava',         3, 2),
    ('Aoife', 3, 3),
--female names b
    ('Babs',        3, 5),
    ('Bailey',      3, 2),
    ('Barbara',     3, 2),
    ('Bea',         3, 2),
    ('Beatrice',    3, 4),
    ('Beatrix',     3, 4),
    ('Becca',       3, 2),
    ('Becky',       3, 2),
    ('Belinda',     3, 4),
    ('Belle',       3, 2),
    ('Bernadette',  3, 2),
    ('Bertha',      3, 2),
    ('Bessie',      3, 2),
    ('Beth',        3, 2),
    ('Bethany',     3, 2),
    ('Betsy',       3, 4),
    ('Betty',       3, 2),
    ('Beverly',     3, 2),
    ('Beyoncé',     3, 5),
    ('Bianca',      3, 2),
    ('Billie',      3, 2),
    ('Blanche',     3, 4),
    ('Blossom',     3, 2),
    ('Blythe',      3, 2),
    ('Bonnie',      3, 2),
    ('Brandy',      3, 2),
    ('Bree',        3, 2),
    ('Brenda',      3, 2),
    ('Bridget',     3, 2),
    ('Brie',        3, 2),
    ('Britney',     3, 2),
    ('Brooke',      3, 2),
    ('Bubbles',     3, 5),
    ('Buffy',       3, 5),
    ('Buttercup',   3, 5),
--female names c
    ('Camila',      3, 2),
    ('Candy',       3, 2),
    ('Cardi',       3, 5),
    ('Carmel',      3, 2),
    ('Carmella',    3, 2),
    ('Carmen',      3, 2),
    ('Caroline',    3, 2),
    ('Caroll',      3, 2),
    ('Cassie',      3, 2),
    ('Charlotte',   3, 2),
    ('Cher',        3, 5),
    ('Chiquita',    3, 4),
    ('Chloe',       3, 2),
    ('Ciara',       3, 4),
    ('Cindy',       3, 2),
    ('Cinnamon',    3, 5),
    ('Clair',       3, 2),
    ('Claire',      3, 2),
    ('Clara',       3, 2),
    ('Cleo',        3, 2),
    ('Coco',        3, 2),
    ('Cotton',      3, 2),
    ('Crystal',     3, 2),
    ('Cupcake',     3, 5),
    ('Cat', 3, 3),

--female names d
    ('Daisy',       3, 2),
    ('Dana',        3, 2),
    ('Daniella',    3, 2),
    ('Danielle',    3, 5),
    ('Daphne',      3, 3),
    ('Darcy',       3, 3),
    ('Davina',      3, 2),
    ('Debby',       3, 2),
    ('Deborah',     3, 5),
    ('Debs',        3, 2),
    ('Deirdre',     3, 3),
    ('Delaney',     3, 2),
    ('Delilah',     3, 2),
    ('Delilah',     3, 2),
    ('Desiree',     3, 2),
    ('Destiny',     3, 2),
    ('Dior',        3, 2),
    ('Dokota',      3, 5),
    ('Dolly',       3, 4),
    ('Donna',       3, 2),
    ('Dorothy',     3, 2),
    ('Dream',       3, 2),
--female names e
    ('Edith',       3, 4),
    ('Edna',        3, 5),
    ('Eevee',       3, 5),
    ('Elaine',      3, 2),
    ('Eleanor',     3, 4),
    ('Eliza',       3, 2),
    ('Elizabeth',   3, 2),
    ('Ellie',       3, 2),
    ('Ember',       3, 2),
    ('Emily',       3, 2),
    ('Emma',        3, 2),
    ('Emmanuella',  3, 3),
    ('Erica',       3, 2),
    ('Esmeralda',   3, 4),
    ('Ester',       3, 4),
    ('Eugenia',     3, 2),
    ('Everly',      3, 2),
]

'''
