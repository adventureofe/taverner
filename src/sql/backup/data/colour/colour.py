import sys
import sqlite3
import pandas as pd

from src.util.sql_table import sql_table_create

from src.sql.data.colour.colour_darkness.colour_darkness_list import colour_darkness_list
from src.sql.data.colour.colour_list import colour_list

cd = {colour_darkness[0]: index+1 for index, colour_darkness in enumerate(colour_darkness_list)}

def colour_create(connection, cursor):
    table_name = "colour"
    columns = [
        "id INTEGER PRIMARY KEY",
        "name TEXT NOT NULL CHECK(length(name) <= 128)",
        "r INTEGER NOT NULL CHECK(r >= 0 AND r <= 255)",
        "g INTEGER NOT NULL CHECK(g >= 0 AND g <= 255)",
        "b INTEGER NOT NULL CHECK(b >= 0 AND b <= 255)",
        "darkness INTEGER NOT NULL"
    ]
    foreign_keys = [
        "FOREIGN KEY(darkness) REFERENCES colour_darkness(id)"
    ]
    values = list(colour_list)  # Assuming colour_list is a list of tuples
    view_query = '''
    SELECT
        tn.id AS id,
        tn.name AS name,
        tn.r AS r,
        tn.g AS g,
        tn.b AS b,
        tn.darkness AS cdid,
        cd.name AS colour_darkness
    FROM colour AS tn
    INNER JOIN colour_darkness AS cd ON tn.darkness = cd.id
    '''

    sql_table_create(connection, cursor, table_name, columns, foreign_keys, values, view_query)
