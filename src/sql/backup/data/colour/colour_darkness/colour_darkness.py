import sys
import sqlite3
import pandas as pd

from src.util.sql_table import sql_table_create

from src.sql.data.colour.colour_darkness.colour_darkness_list import colour_darkness_list

def colour_darkness_create(connection, cursor):
    table_name = "colour_darkness"
    columns = [
        "id INTEGER PRIMARY KEY",
        "name TEXT NOT NULL CHECK(length(name) <= 128)"
    ]
    foreign_keys = []  # No foreign keys for this table
    values = list(colour_darkness_list)  # Assuming colour_darkness_list is already a list of tuples
    view_query = '''
    SELECT
        tn.id AS id,
        tn.name AS name
    FROM colour_darkness AS tn
    '''
    sql_table_create(connection, cursor, table_name, columns, foreign_keys, values, view_query)
