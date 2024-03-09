.mode column
.headers ON
.separator ROW "\n"
.nullvalue NULL

-- use sqlite3 on taverner.db
-- use .read to read sql files

DROP TABLE IF EXISTS moveset;
CREATE TABLE moveset
(
    move INTEGER NOT NULL, 
    element INTEGER NOT NULL, 
    species INTEGER NOT NULL,
    level INTEGER NOT NULL,

    FOREIGN KEY(move) REFERENCES move(id),
    FOREIGN KEY(element) REFERENCES element(id),
    FOREIGN KEY(species) REFERENCES species(id),
    PRIMARY KEY(move, element, species, level)
);
