import sys
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from sql.utility.sql_table_funcs import sql_table_drop, sql_table_print, sql_change_print

#from sql.data.language.name.name_origin.name_origin import name_origin_create
#from sql.data.language.name.name_place.name_place import name_place_create

from sql.generate.generate_colour import generate_colour
'''
from sql.generate.generate_element import generate_element
from sql.generate.generate_item import generate_item
from sql.generate.generate_species import generate_species
from sql.generate.generate_move import generate_move
from sql.generate.generate_person_name import generate_person_name
from sql.generate.generate_adjective import generate_adjective
from sql.generate.generate_moveset import generate_moveset
'''

func_list = [
    #(name_origin_create, "name_origin"),
    #(name_place_create, "name_place")
]

def generate_all_sql_tables(connection, cursor, func_list=func_list):
    generate_colour(connection, cursor)
    #generate_element(connection, cursor)
    #generate_item(connection, cursor)
    #generate_species(connection, cursor)
    #generate_move(connection, cursor)
    #generate_person_name(connection, cursor)
    #generate_adjective(connection, cursor)
    #generate_moveset(connection, cursor)
    """Creates tables using the provided list of creation functions."""
    for create_func, table_name in func_list:
        try:
            create_func(connection, cursor)
        except Exception as e:
            print(f"ERROR: generate_all {table_name}: {e}")
            continue  # Proceed to the next table
