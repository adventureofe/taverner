import sys
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from sql.utility.sql_table_funcs import sql_table_drop, sql_table_print, sql_change_print

from sql.utility.generate_function import generate_function


from sql.data.language.adjective.element_adjective.element_adjective import element_adjective_create

from sql.data.element.element_effectiveness.element_effectiveness import element_effectiveness_create

from sql.data.element.element_effectiveness.element_effectiveness_type.element_effectiveness_type import element_effectiveness_type_create

from sql.data.element.element import element_create

from sql.data.element.element_type.element_type import element_type_create


func_list = [
    (element_adjective_create, "element_adjective"),
    (element_type_create, "element_type"),
    (element_create, "element"),
    (element_effectiveness_type_create, "element_effectiveness_type"),
    (element_effectiveness_create, "element_effectiveness"),
]

def generate_element(connection, cursor, func_list=func_list):
    generate_function(connection, cursor, func_list)
