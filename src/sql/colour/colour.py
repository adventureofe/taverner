import sys
import sqlite3
import pandas as pd
from src.sql.sql_table import SQLTable
from src.sql.sql_table import Config

from src.sql.colour.colour_list import colour_list as values

def colour_create(connection, cursor, name="colour", values=values):
    print(Config.id)
    table = SQLTable(
        name=name,

        columns=[
            Config.id,
            Config.name,
            "r INTEGER NOT NULL CHECK(r >= 0 AND r <= 255)",
            "g INTEGER NOT NULL CHECK(g >= 0 AND g <= 255)",
            "b INTEGER NOT NULL CHECK(b >= 0 AND b <= 255)",
            "darkness INTEGER NOT NULL",
            "base INTEGER NOT NULL",
        ],

        foreign_keys=[
            "FOREIGN KEY(darkness) REFERENCES colour_darkness(id)",
            "FOREIGN KEY(base) REFERENCES colour_base(id)"
        ],

        values=values,

        view_query=f'''
        SELECT
        t.id AS id,
        t.name AS name,
        t.r AS r,
        t.g AS g,
        t.b AS b,

        t.darkness AS did,
        d.name AS darkness,

        t.base AS bid,
        b.name AS base

        FROM {name} AS t
        INNER JOIN colour_darkness AS d ON t.darkness = d.id
        INNER JOIN colour_base AS b ON t.base = b.id;
        ''',
        insert_query=f"INSERT INTO {name} (name, r, g, b, darkness, base) VALUES (?, ?, ?, ?, ?, ?)"
    )

    table.create(connection, cursor)
    table.change_print(connection, cursor)
    return table
