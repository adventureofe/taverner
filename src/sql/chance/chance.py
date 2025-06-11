import sys
import sqlite3
import pandas as pd
from src.sql.sql_table import SQLTable
from src.sql.sql_table import Config

from src.sql.sql_table import base_table_create

from src.sql.chance.chance_list import chance_list as values

def chance_create(connection, cursor, name="chance", values=values):
    table = SQLTable(
        name=name,

        columns=[
            Config.id,
            Config.name,
            "percent INTEGER NOT NULL"
        ],

        foreign_keys=[],

        values=values,

        view_query=f'''
        SELECT
        t.id AS id,
        t.name AS name,
        t.percent AS chance


        from {name} AS t
        ''',
        insert_query=f"INSERT INTO {name} (name, percent) VALUES (?, ?)"
    )
    table.create(connection, cursor)
    table.change_print(connection, cursor)
    return table
