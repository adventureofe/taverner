import sys
import sqlite3
import pandas as pd
from src.sql.sql_table import SQLTable

from src.sql.colour.colour_list import colour_list

def colour_create(connection, cursor, name="colour", values=colour_list):
    table = SQLTable(
        name="colour",

        columns=[
            "id INTEGER PRIMARY KEY AUTOINCREMENT",
            "name TEXT NOT NULL CHECK(length(name) <= 128)",
            "r INTEGER NOT NULL CHECK(r >= 0 AND r <= 255)",
            "g INTEGER NOT NULL CHECK(g >= 0 AND g <= 255)",
            "b INTEGER NOT NULL CHECK(b >= 0 AND b <= 255)",
            "darkness INTEGER NOT NULL",
            "base INTEGER NOT NULL"
        ],

        foreign_keys=[
            "FOREIGN KEY(darkness) REFERENCES colour_darkness(id)",
            "FOREIGN KEY(base) REFERENCES colour_base(id)"
        ],

        values=values,

        view_query='''
        SELECT
        tn.id AS id,
        tn.name AS name,
        tn.r AS r,
        tn.g AS g,
        tn.b AS b,

        tn.darkness AS cdid,
        cd.name AS colour_darkness,

        tn.base AS cbid,
        cb.name AS colour_base

        FROM colour AS tn
        INNER JOIN colour_darkness AS cd ON tn.darkness = cd.id
        INNER JOIN colour_base AS cb ON tn.base = cb.id
        ''',
        insert_query="INSERT INTO colour (name, r, g, b, darkness, base) VALUES (?, ?, ?, ?, ?, ?)"

    )

    table.create(connection, cursor)
    table.change_print(connection, cursor)
    return table
