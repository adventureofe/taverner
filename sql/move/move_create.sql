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
    name TEXT NOT NULL
);

DROP TABLE IF EXISTS move_category;
CREATE TABLE move_category
(
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL
);

DROP TABLE IF EXISTS move_effect;
CREATE TABLE move_effect
(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

DROP TABLE IF EXISTS move_ai_prompt;
CREATE TABLE move_ai_prompt
(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

DROP TABLE IF EXISTS move;
CREATE TABLE move
(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
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
