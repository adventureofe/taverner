import sys
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from sql.utility.sql_table_funcs import sql_table_drop, sql_table_print, sql_change_print

from sql.utility.generate_function import generate_function

from sql.data.moveset.moveset_chance.moveset_chance import moveset_chance_create

from sql.data.moveset.species_moveset import species_moveset_create

func_list = [
    (moveset_chance_create, "moveset_chance"),
    (species_moveset_create, "species_moveset"),
]

def generate_moveset(connection, cursor, func_list=func_list):
    generate_function(connection, cursor, func_list)
