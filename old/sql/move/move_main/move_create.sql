.mode column
.headers ON
.separator ROW "\n"
.nullvalue NULL

-- use sqlite3 on taverner.db
-- use .read to read sql files

DROP TABLE IF EXISTS move_type;
CREATE TABLE move_type
(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL CHECK(length(name) < 64)
);

DROP TABLE IF EXISTS move_category;
CREATE TABLE move_category
(
   id INTEGER PRIMARY KEY,
   name TEXT NOT NULL CHECK(length(name) < 64)
);

DROP TABLE IF EXISTS move_effect;
CREATE TABLE move_effect
(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL CHECK(length(name) < 64)
);

DROP TABLE IF EXISTS move_ai_prompt;
CREATE TABLE move_ai_prompt
(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL CHECK(length(name) < 64)
);

DROP TABLE IF EXISTS move;
CREATE TABLE move
(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL CHECK(length(name) < 64),
    element INTEGER NOT NULL,
    type INTEGER NOT NULL,
    priority INTEGER NOT NULL,
    category INTEGER NOT NULL,
    ai_prompt INTEGER NOT NULL,
    effect INTEGER NOT NULL,
    chance INTEGER NOT NULL,
    FOREIGN KEY(element) REFERENCES element(id),
    FOREIGN KEY(type) REFERENCES move_type(id),
    FOREIGN KEY(effect) REFERENCES move_effect(id),
    FOREIGN KEY(category) REFERENCES move_category(id),
    FOREIGN KEY (ai_prompt) REFERENCES move_ai_prompt(id)
);

CREATE TRIGGER check_move_element
BEFORE INSERT ON move
FOR EACH ROW
WHEN NEW.element > (SELECT COUNT(*) FROM element) OR NEW.element < 1
BEGIN
    SELECT RAISE(FAIL, 'ERROR IN move_create.sql: INVALID element VALUE');
END;

CREATE TRIGGER check_move_type
BEFORE INSERT ON move
FOR EACH ROW
WHEN NEW.type > (SELECT COUNT(*) FROM move_type) OR NEW.type < 1
BEGIN
    SELECT RAISE(FAIL, 'ERROR IN move_create.sql: INVALID move_type VALUE');
END;

CREATE TRIGGER check_move_category
BEFORE INSERT ON move
FOR EACH ROW
WHEN NEW.category > (SELECT COUNT(*) FROM move_category) OR NEW.category < 1
BEGIN
    SELECT RAISE(FAIL, 'ERROR IN move_create.sql: INVALID move_category VALUE');
END;

CREATE TRIGGER check_move_effect
BEFORE INSERT ON move
FOR EACH ROW
WHEN NEW.effect > (SELECT COUNT(*) FROM move_effect) OR NEW.effect < 1
BEGIN
    SELECT RAISE(FAIL, 'ERROR IN move_create.sql: INVALID move_effect VALUE');
END;

CREATE TRIGGER check_move_ai_prompt
BEFORE INSERT ON move
FOR EACH ROW
WHEN NEW.ai_prompt > (SELECT COUNT(*) FROM move_ai_prompt) OR NEW.ai_prompt < 1
BEGIN
    SELECT RAISE(FAIL, 'ERROR IN move_create.sql: INVALID move_ai_prompt VALUE');
END;
