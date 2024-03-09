DROP TABLE IF EXISTS food;
CREATE TABLE food
(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL CHECK(length(name) <= 64),
    rarity INTEGER NOT NULL,
    colour INTEGER NOT NULL,
    price INTEGER NOT NULL,
    FOREIGN KEY(colour) REFERENCES colour(id)
);
