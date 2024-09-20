import sys
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

from src.util.sql_util import sql_table_drop, sql_table_print, sql_change_print, sql_to_df, sql_add_funcs

from src.sql.create.funcs.colour_create import colour_create

func_list = [
    colour_create
]

def sql_create_all(connection, cursor, func_list=func_list):
    for create_func in func_list:
        try:
            create_func(connection, cursor)
        except Exception as e:
            print(f"ERROR: generate_all {table_name}: {e}")
            continue  # Proceed to the next table
