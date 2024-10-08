import sys
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from sql.utility.sql_table_funcs import sql_table_drop, sql_table_print, sql_change_print

from sql.utility.generate_function import generate_function

from sql.data.colour.colour_darkness.colour_darkness import colour_darkness_create

from ssql.data.colour.colour import colour_create

from sql.data.language.adjective.colour_adjective.colour_adjective import colour_adjective_create


func_list = [
    (colour_darkness_create, "colour_darkness"),
    (colour_create, "colour"),
    (colour_adjective_create, "colour_adjective"),
]

def generate_colour(connection, cursor, func_list=func_list):
    generate_function(connection, cursor, func_list)
