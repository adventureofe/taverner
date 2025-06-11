#import sys
import sqlite3
import pandas as pd
from src.sql.sql_table import SQLTable
from src.sql.sql_table import Config

from src.sql.moveset_species.moveset_species_list import moveset_species_list as values

def moveset_species_create(connection, cursor, name="moveset_species", values=values):
    table = SQLTable(
        name="moveset_species",

        columns=[
            "species INTEGER NOT NULL",
            "move INTEGER NOT NULL",
            "level INTEGER NOT NULL",
            "chance INTEGER NOT NULL"
        ],

        foreign_keys=[
            "FOREIGN KEY (species) REFERENCES species(id)",
            "FOREIGN KEY (move) REFERENCES move(id)",
            "FOREIGN KEY (chance) REFERENCES chance(id)",
            "PRIMARY KEY (species, move)"
        ],

        values=values,

        view_query=f'''
        SELECT
        t.species AS sid,
        s.name AS species,

        t.move AS mid,
        m.name AS move,

        t.level AS level,

        t.chance AS cid,
        c.name AS chance

        FROM {name} AS t

        INNER JOIN species AS s ON t.species = s.id
        INNER JOIN move AS m ON t.move = m.id
        INNER JOIN chance AS c ON t.chance= c.id
        ''',

        insert_query = f"INSERT INTO {name} (species, move, level, chance) VALUES (?, ?, ?, ?)"
    )

    table.create(connection, cursor)
    table.change_print(connection, cursor)
    return table
