DROP TABLE IF EXISTS element_effectiveness;
CREATE TABLE element_effectiveness
(
    attacker INTEGER NOT NULL,
    defender INTEGER NOT NULL,
    effectiveness INTEGER NOT NULL,
    FOREIGN KEY (attacker) REFERENCES element(id),
    FOREIGN KEY (defender) REFERENCES element(id),
    PRIMARY KEY (attacker, defender)
);
