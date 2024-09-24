import sys
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from sql.utility.sql_table_funcs import sql_table_drop, sql_table_print, sql_change_print

from sql.utility.generate_function import generate_function

from sql.data.species.species_family.species_family import species_family_create

from sql.data.species.species_type.species_type import species_type_create

from sql.data.species.species import species_create

func_list = [
    (species_family_create, "species_family"),
    (species_type_create, "species_type"),
    (species_create, "species"),

]

def generate_species(connection, cursor, func_list=func_list):
    generate_function(connection, cursor, func_list)
