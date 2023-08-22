DROP TABLE IF EXISTS colour;
CREATE TABLE colour
(
       id INTEGER PRIMARY KEY,
       name TEXT NOT NULL,
       r INTEGER NOT NULL CHECK(r >= 0 AND r <= 255),
       g INTEGER NOT NULL CHECK(g >= 0 AND g <= 255),
       b INTEGER NOT NULL CHECK(b >= 0 AND b <= 255)
);
