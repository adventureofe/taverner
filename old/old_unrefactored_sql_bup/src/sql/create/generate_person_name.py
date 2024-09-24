import sys
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from sql.utility.sql_table_funcs import sql_table_drop, sql_table_print, sql_change_print

from sql.data.language.name.person_name.person_name_gender.person_name_gender import person_name_gender_create

from sql.data.language.name.person_name.person_name_category.person_name_category import person_name_category_create

from sql.data.language.name.person_name.person_name import person_name_create

from sql.utility.generate_function import generate_function


func_list = [
    (person_name_gender_create, "person_name_gender"),
    (person_name_category_create, "person_name_category"),
    (person_name_create, "person_name"),
]

def generate_person_name(connection, cursor, func_list=func_list):
    generate_function(connection, cursor, func_list)
