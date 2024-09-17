import sys
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from sql.utility.sql_table_funcs import sql_table_drop, sql_table_print, sql_change_print

from sql.utility.generate_function import generate_function

from sql.data.language.adjective.adjective import adjective_create


from sql.data.language.adjective.adjective_connotation.adjective_connotation import adjective_connotation_create

func_list = [
    (adjective_connotation_create, "adjective_connotation"),
    (adjective_create, "adjective"),
]

def generate_adjective(connection, cursor, func_list=func_list):
    generate_function(connection, cursor, func_list)
