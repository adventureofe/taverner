import sys
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from sql.utility.sql_table_funcs import sql_table_drop, sql_table_print, sql_change_print

from sql.utility..generate_function import generate_function

from sql.data.move.move_type.move_type import move_type_create

from sql.data.move.move_category.move_category import move_category_create

from sql.data.move.move import move_create


func_list = [
    (move_type_create, "move_type"),
    (move_category_create, "move_category"),
    (move_create, "move"),
]

def generate_move(connection, cursor, func_list=func_list):
    generate_function(connection, cursor, func_list)
