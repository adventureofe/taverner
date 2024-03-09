INSERT INTO colour_simile_type(name)
VAlUES
    ('none'),
    ('a'),
    ('an'),
    ('the');



INSERT INTO colour(name, r, g, b, describer, simile, simile_type)
VALUES
    ('colourless', 128, 128, 128, 'none',       'nothing',  1), -- 01
    ('pink',       255, 192, 203, 'romantic',   'flamingo', 2), -- 02
    ('magenta',    255, 000, 255, 'vibrant',    'hibiscus', 2), -- 03
    ('light grey', 192, 192, 192, 'subtle',     'cloud',    2), -- 04
    ('orange',     255, 128, 000, 'warm',       'orange',   3), -- 05
    ('brown',      128, 064, 000, 'rustic',     'oak',      3), -- 06
    ('yellow',     255, 255, 000, 'energetic',  'banana',   2), -- 07
    ('black',      000, 000, 000, 'sleek',      'night',    4), -- 08
    ('red',        255, 000, 000, 'passionate', 'rose',     2), -- 09
    ('white',      255, 255, 255, 'pure',       'snow',     1), -- 10
    ('cyan',       000, 255, 255, 'calm',       'tropics',  4), -- 11
    ('dark grey',  064, 064, 064, 'somber',     'storm',    2), -- 12
    ('maroon',     128, 000, 000, 'rich',       'wine',     1), -- 13
    ('grey',       128, 128, 128, 'subdued',    'elephant', 3), -- 14
    ('green',      000, 255, 000, 'fresh',      'grass',    1), -- 15
    ('purple',     128, 000, 128, 'royal',      'grape',    2), -- 16
    ('lime',       096, 255, 096, 'zesty',      'lime',     2), -- 16
    ('dark green', 000, 096, 000, 'dank',       'pine',     1), -- 18
    ('blue',       000, 000, 255, 'tranquil',   'ocean',    4); -- 19
