import sys
import sqlite3
import pandas as pd
from src.sql.sql_table import SQLTable
from src.sql.sql_table import Config

from src.sql.move.move_list import move_list as values

def move_create(connection, cursor, name="move", values=values):
    table = SQLTable(
        name="move",

        columns=[
            Config.id,
            Config.text("name"),
            "power INTEGER NOT NULL",
            "element INTEGER NOT NULL",
            "type INTEGER NOT NULL",
            "category INTEGER NOT NULL",
            "priority INTEGER NOT NULL",
            Config.text("description"),
        ],

        foreign_keys=[
            "FOREIGN KEY(element) REFERENCES element(id)",
            "FOREIGN KEY(type) REFERENCES move_type(id)",
            "FOREIGN KEY(category) REFERENCES move_category(id)"
        ],

        values=values,

        view_query=f'''
        SELECT
        t.id AS id,
        t.name AS name,
        t.power AS power,

        t.element AS eid,
        e.name AS element,

        t.type as tid,
        mt.name as type,

        t.category as cid,
        c.name as category,

        t.priority as priority,
        t.description as description

        FROM {name} AS t
        INNER JOIN element AS e on t.element = e.id
        INNER JOIN move_type AS mt on t.type = mt.id
        INNER JOIN move_category AS c on t.category = c.id
        ''',

        insert_query = f"INSERT INTO {name} (name, power, element, type, category, priority, description) VALUES (?, ?, ?, ?, ?, ?, ?)"
    )

    table.create(connection, cursor)
    table.change_print(connection, cursor)
    return table
