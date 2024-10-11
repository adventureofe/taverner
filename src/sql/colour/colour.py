import sys
import sqlite3
import pandas as pd
from src.sql.sql_table import SQLTable
from src.sql.sql_table import Config

from src.sql.colour.colour_list import colour_list

def colour_create(connection, cursor, name="colour", values=colour_list):
    print(Config.id)
    table = SQLTable(
        name="colour",

        columns=[
            Config.id,
            Config.text("name"),
            "r INTEGER NOT NULL CHECK(r >= 0 AND r <= 255)",
            "g INTEGER NOT NULL CHECK(g >= 0 AND g <= 255)",
            "b INTEGER NOT NULL CHECK(b >= 0 AND b <= 255)",
            "hex TEXT",
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
        t.hex AS hex,

        t.darkness AS did,
        d.name AS darkness,

        t.base AS bid,
        b.name AS base

        FROM {name} AS t
        INNER JOIN colour_darkness AS d ON t.darkness = d.id
        INNER JOIN colour_base AS b ON t.base = b.id;
        ''',
        insert_query=f"INSERT INTO {name} (name, r, g, b, darkness, base) VALUES (?, ?, ?, ?, ?, ?)",

        triggers=f'''
        CREATE TRIGGER generate_hex_code
        AFTER INSERT ON {name}
        BEGIN
            UPDATE {name}
            SET hex = printf('#%02X%02X%02X', NEW.r, NEW.g, NEW.b)
            WHERE id = NEW.id;
        END;
        '''
    )

    table.create(connection, cursor)

    # Debug: Check if the trigger is created
    cursor.execute("SELECT name FROM sqlite_master WHERE type='trigger' AND name='generate_hex_code';")
    print(cursor.fetchall())

    # Debug: Print current state of the table
    table.change_print(connection, cursor)

    return table
