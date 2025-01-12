import sys
import sqlite3
import pandas as pd
from src.sql.sql_table import SQLTable
from src.sql.sql_table import Config

from src.sql.species.species_list import species_list as values

def species_create(connection, cursor, name="species", values=values):
    print(Config.id)

    table = SQLTable(

        name=name,

        columns=[
            Config.id,
            "type INTEGER NOT NULL",
            "lineage INTEGER NOT NULL",
            "position INTEGER NOT NULL",
            Config.name,
            "name2 TEXT NOT NULL",
            "height_min INTEGER NOT NULL",
            "height_max INTEGER NOT NULL",
            "weight_min INTEGER NOT NULL",
            "weight_max INTEGER NOT NULL",
        ],

        foreign_keys=[
            "FOREIGN KEY(type) REFERENCES species_type(id)",
            "CHECK (height_min <= height_max)",
            "CHECK (weight_min <= weight_max)"
        ],

        values=values,

        # removed
        # t.family AS fid,
        # f.name AS family,
        # INNER JOIN species_family AS f ON t.family = f.id;


        view_query=f'''
        SELECT
        t.id AS id,

        t.type AS tid,
        st.name AS type,

        t.lineage AS lineage,
        t.position AS position,


        t.name AS name,
        t.height_min AS height_min,
        t.height_max AS height_max,
        t.weight_min AS weight_min,
        t.weight_max AS weight_max

        from {name} AS t
        INNER JOIN species_type AS st ON t.type = st.id;
        ''',

        insert_query = f"INSERT INTO {name} (type, lineage, position, name, name2, height_min, height_max, weight_min, weight_max) VALUES (?, ?, ?, ?, ?, ? ,? ,? ,?)"
    )

    table.create(connection, cursor)
    table.change_print(connection, cursor)
    return table
