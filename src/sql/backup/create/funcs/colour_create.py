import sys
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

from src.sql.data.colour.colour_darkness.colour_darkness import colour_darkness_create

from src.sql.data.colour.colour import colour_create

func_list = [
    colour_create, 
    colour_darkness_create,
]

def sql_table_add_funcs(connection, cursor, func_list):
    for create_func in func_list:
        table_name = create_func.__name__.replace('create_', '')  # Derive table name from function name
        try:
            create_func(connection, cursor)  # Call the function to create the table
        except Exception as e:
            print(f"ERROR: generate_all {table_name}: {e}")
            continue  # Proceed to the next table

def colour_create(connection, cursor, func_list=func_list):
    sql_table_add_funcs(connection, cursor, func_list)
