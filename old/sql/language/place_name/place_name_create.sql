DROP TABLE IF EXISTS place_name_ending_geography;
CREATE TABlE place_name_ending_geography
(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL CHECK(length(name) <= 64)
);

DROP TABLE IF EXISTS place_name_ending_region;
CREATE TABlE place_name_ending_region
(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL CHECK(length(name) <= 64)
);

DROP TABLE IF EXISTS place_name_ending;
CREATE TABlE place_name_ending
(
    id INTEGER PRIMARY KEY,
    geography INTEGER NOT NULL,
    region INTEGER NOT NULL,
    syllable INTEGER NOT NULL,
    FOREIGN KEY(geography) REFERENCES place_name_ending_geography    
    FOREIGN KEY(region) REFERENCES place_name_ending_region    
);

CREATE TRIGGER check_place_name_ending_geography
BEFORE INSERT ON place_name_ending
FOR EACH ROW
WHEN NEW.geography > (SELECT COUNT(*) FROM place_name_ending_geography) OR NEW.geography < 1
BEGIN
    SELECT RAISE(FAIL, 'ERROR IN place_name_create.sql: INVALID geography VALUE');
END;

CREATE TRIGGER check_place_name_ending_region
BEFORE INSERT ON place_name_ending
FOR EACH ROW
WHEN NEW.region > (SELECT COUNT(*) FROM place_name_ending_region) OR NEW.region < 1
BEGIN
    SELECT RAISE(FAIL, 'ERROR IN place_name_create.sql: INVALID region VALUE');
END;
