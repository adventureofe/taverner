.mode column
.headers ON
.separator ROW "\n"
.nullvalue NULL

-- use sqlite3 on taverner.db
-- use .read to read sql files

INSERT INTO move_type(name)
VALUES
    ('typeless'),
    ('physical'),
    ('special');

INSERT INTO move_category(name)
VALUES
    ('none'),  --01
    ('misc'),  --02
    ('tool'),  --03
    ('hand'),  --04
    ('leg'),   --05
    ('bolt'),  --06
    ('ball'),  --07
    ('blast'), --08
    ('spit'),  --09
    ('arm'),   --10
    ('whip'),  --11
    ('mouth'), --12
    ('head');  --13

INSERT INTO move_effect(name)
VALUES
    ('none'),     --01
    ('switch'),   --02
    ('trap'),     --03
    ('burn'),     --04
    ('paralyze'), --05
    ('terrain'),  --06
    ('prevent');  --07

INSERT INTO move_ai_prompt(name)
VALUES
    ('none'),     --01
    ('attack'),   --02
    ('setup'),    --03
    ('heal'),     --04
    ('status'),   --05
    ('terrain');  --06

INSERT INTO move(name, element, type, priority, category, ai_prompt, effect, chance)
VALUES
--01.typeless
    ('thud',            01, 1, 1, 01, 01, 01, 100), -- 1
--02.alien
    ('probe',           02, 2, 1, 03, 02, 01, 100), -- 2
    ('death ray',       02, 3, 1, 08, 05, 01, 100), -- 3
    ('plasma ball',     02, 3, 1, 07, 02, 01, 100), -- 4
    ('plasma fist',     02, 2, 1, 04, 02, 01, 100), -- 5
--03.air
    ('tornado punch',   03, 2, 1, 04, 02, 01, 100), -- 6
    ('gust',            03, 3, 1, 08, 02, 01, 100), -- 7
    ('hurricane',       03, 3, 1, 08, 03, 01, 100), -- 8
    ('maelstrom',       03, 3, 1, 02, 02, 01, 100), -- 9
--04.chaos
    ('discombobulate',  04, 2, 1, 08, 05, 01, 90), -- 10
    ('warp',            04, 3, 1, 08, 02, 01, 90), -- 11
    ('perplex',         04, 3, 0, 13, 02, 01, 90), -- 12
    ('reality shift',   04, 2, 1, 02, 06, 01, 90), -- 13
--05.earth
    ('stomp',           05, 2, 1, 05, 02, 01, 100), -- 14
    ('stalactite',      05, 3, 1, 06, 02, 01, 100), -- 15
    ('earthquake',      05, 2, 1, 05, 06, 01, 100), -- 16
    ('mud shot',        05, 3, 1, 08, 02, 01, 100), -- 17
--06.electricity
    ('thunder punch',   06, 2, 1, 04, 02, 01, 100), -- 18
    ('lightning bolt',  06, 3, 1, 06, 02, 01, 100), -- 19
    ('thunder shock',   06, 3, 1, 08, 02, 01, 100), -- 20
    ('electrify',       06, 2, 1, 04, 05, 01, 100), -- 21
--07.evil
    ('backstab',        07, 2, 1, 03, 02, 01, 100), -- 22
    ('booby trap',      07, 3, 0, 03, 03, 01, 100), -- 23
    ('bite',            07, 2, 1, 12, 02, 01, 100), -- 24
    ('sucker punch',    07, 2, 2, 04, 02, 01, 100), -- 25
--08.fire
    ('fire punch',      08, 2, 1, 04, 02, 01, 100),
    ('fire ball',       08, 3, 1, 07, 02, 01, 100),
    ('flame kick',      08, 2, 1, 05, 02, 01, 100),
    ('eruption',        08, 3, 1, 02, 06, 01, 100),
--09.holiness
    ('light punch',     09, 2, 1, 04, 02, 01, 100),
    ('smite',           09, 3, 1, 06, 02, 01, 100),
    ('sacred fires',    09, 3, 1, 08, 03, 01, 100),
    ('judgement',       09, 2, 1, 13, 06, 01, 100),
--10.ice
    ('ice punch',       10, 2, 1, 04, 02, 01, 100),
    ('snow ball',       10, 3, 1, 07, 02, 01, 100),
    ('hail',            10, 3, 1, 02, 06, 01, 100),
    ('frost breath',    10, 3, 1, 09, 02, 01, 100),
--11.metal
    ('metal punch',     11, 2, 1, 04, 02, 01, 100),
    ('bullet',          11, 3, 2, 06, 02, 01, 100),
    ('slam',            11, 2, 1, 02, 02, 01, 100),
    ('shard',           11, 3, 1, 03, 02, 01, 100),
--12.mutation
    ('tentacle slap',   12, 2, 1, 11, 02, 01, 100),
    ('smileball',       12, 3, 1, 07, 02, 01, 100),
    ('constriction',    12, 2, 1, 10, 02, 01, 100),
    ('corrode',         12, 2, 1, 09, 06, 01, 100),
--13.normal
    ('smack',           13, 2, 1, 04, 02, 01, 100),
    ('mind blast',      13, 3, 1, 08, 02, 01, 100),
    ('headbutt',        13, 2, 1, 13, 02, 01, 100),
    ('roundhouse kick', 13, 2, 1, 05, 02, 01, 100),
--14.plant
    ('vine whip',       14, 2, 1, 11, 02, 01, 100),
    ('leaf bolt',       14, 3, 1, 06, 02, 01, 100),
    ('branch swing',    14, 2, 1, 10, 02, 01, 100),
    ('leaf storm',      14, 3, 1, 08, 02, 01, 100),
--15.poison
    ('toxic touch',     15, 2, 1, 04, 02, 01, 100),
    ('venom spit',      15, 3, 1, 09, 02, 01, 100),
    ('poison fangs',    15, 2, 1, 12, 02, 01, 100),
    ('poison barb',     15, 3, 1, 02, 02, 01, 100),
--16.radiation
    ('atom punch',      16, 2, 1, 04, 02, 01, 100),
    ('atomic blast',    16, 3, 0, 08, 02, 01, 100),
    ('atom bomb',       16, 3, 1, 03, 06, 01, 100),
    ('atom kick',       16, 2, 1, 05, 02, 01, 100),
--17.undead
    ('eat',             17, 2, 1, 12, 02, 01, 100),
    ('arm throw',       17, 3, 1, 03, 02, 01, 100),
    ('infected spit',   17, 3, 1, 09, 02, 01, 100),
    ('blood ball',      17, 3, 1, 07, 02, 01, 100),
--18.water
    ('squirt',          18, 3, 1, 08, 02, 01, 100),
    ('water punch',     18, 2, 1, 04, 02, 01, 100),
    ('water bolt',      18, 3, 1, 06, 02, 01, 100),
    ('water kick',      18, 2, 1, 05, 02, 01, 100);
