import sys
import sqlite3
import pandas as pd
from src.sql.sql_table import SQLTable
from src.sql.sql_table import base_table_create

from src.sql.colour_darkness.colour_darkness_list import colour_darkness_list

def colour_darkness_create(
        connection,
        cursor,
        name="colour_darkness",
        values=colour_darkness_list):
    return base_table_create(connection, cursor, name, values)
