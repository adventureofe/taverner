import sys
import sqlite3
import pandas as pd
from src.sql.sql_table import SQLTable
from src.sql.sql_table import Config

from src.sql.species_type.species_type_list import species_type_list as values

def species_type_create(connection, cursor, name="species_type", values=values):
    print(Config.id)

    table = SQLTable(

        name=name,

        columns=[
            Config.id,
            Config.name,
            "family INTEGER NOT NULL",
        ],

        foreign_keys=[
            "FOREIGN KEY(family) REFERENCES species_family(id)",
        ],

        values=values,

        view_query=f'''
        SELECT
        t.id AS id,

        t.name AS name,

        t.family AS fid,
        f.name AS family

        from {name} AS t
        INNER JOIN species_family AS f ON t.family = f.id;
        ''',

        insert_query = f"INSERT INTO {name} (name, family) VALUES (?, ?)"
    )

    table.create(connection, cursor)
    table.change_print(connection, cursor)
    return table
