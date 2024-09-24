import sys
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from sql.utility.sql_table_funcs import sql_table_drop, sql_table_print, sql_change_print

from sql.utility.generate_function import generate_function

from sql.data.item.item import item_create
from sql.data.item.item_diet.item_diet import item_diet_create

from sql.data.item.item_diet.item_diet_consume.item_diet_consume import item_diet_consume_create


func_list = [
    (item_diet_consume_create, "item_diet_consume"),
    (item_diet_create, "item_diet"),
    (item_create, "item")
]

def generate_item(connection, cursor, func_list=func_list):
    generate_function(connection, cursor, func_list)
