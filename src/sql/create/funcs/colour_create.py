import sys
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


from src.util.sql_util import sql_table_drop, sql_table_print, sql_change_print, sql_to_df, sql_add_funcs

from src.sql.data.colour.colour_darkness.colour_darkness import colour_darkness_create

from src.sql.data.colour.colour import colour_create



func_list = [
    colour_create, 
    colour_darkness_create,
]

def colour_create(connection, cursor, func_list=func_list):
    sql_add_funcs(connection, cursor, func_list)
