#!/usr/bin/env python3

import sys
import sqlite3
import pandas as pd
from src.sql.sql_table import SQLTable
from src.sql.sql_table import Config

from src.sql.element.element_list import element_list

def element_create(connection, cursor, name="element", values=element_list):
    table = SQLTable(
        name="element",

        columns=[
            Config.id,
            Config.text("name"),
            "colour INTEGER NOT NULL",
            "type INTEGER NOT NULL"
        ],

        foreign_keys=[
            "FOREIGN KEY (colour) REFERENCES colour(id)",
            "FOREIGN KEY (type) REFERENCES move_type(id)"
        ],

        values=values,

        view_query=f'''
        SELECT
        t.id AS id,
        t.name AS name,

        t.colour AS cid,
        c.name AS colour,

        t.type as tid,
        m.name as type

        FROM {name} AS t
        INNER JOIN colour AS c ON t.colour = c.id
        INNER JOIN move_type AS m ON t.type = m.id
        ''',

        insert_query = f"INSERT INTO {name} (name, colour, type) VALUES (?, ?, ?)"
    )

    table.create(connection, cursor)
    table.change_print(connection, cursor)
    return table
