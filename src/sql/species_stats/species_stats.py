import sys
import sqlite3
import pandas as pd
from src.sql.sql_table import SQLTable
from src.sql.sql_table import Config

from src.sql.species.species_list import species_list as values

def element_effectiveness_create(connection, cursor, name="species_stats", values=values):
    table = SQLTable(
        name="species_stats",

        columns=[
            "species INTEGER NOT NULL",
            "physical_atk INTEGER NOT NULL",
            "physical_def INTEGER NOT NULL",
            "magic_atk INTEGER NOT NULL",
            "magic_def INTEGER NOT NULL",
            "speed INTEGER NOT NULL"
        ],

        foreign_keys=[
            "FOREIGN KEY (species) REFERENCES species(id)",
            "FOREIGN KEY (effectiveness) REFERENCES effectiveness_type(id)",
            "PRIMARY KEY species)"
        ],

        values=values,

        view_query=f'''
        SELECT
        t.attacker AS atk,
        e1.name AS attacker,

        t.defender AS def,
        e2.name AS defender,

        t.effectiveness AS eid,
        et.name As effectiveness

        FROM {name} AS t

        INNER JOIN element AS e1 ON t.attacker = e1.id
        INNER JOIN element AS e2 ON t.defender = e2.id
        INNER JOIN effectiveness_type AS et ON et.id = t.effectiveness;
        ''',

        insert_query = f"INSERT INTO {name} (attacker, defender, effectiveness) VALUES (?, ?, ?)"

        )

    table.create(connection, cursor)
    table.change_print(connection, cursor)
    return table
