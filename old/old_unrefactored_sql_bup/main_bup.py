import sys
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from sql.utility.sql_table_funcs import sql_table_drop, sql_table_print, sql_change_print

from sql.generate.colour.colour_darkness.colour_darkness import colour_darkness_create

from sql.generate.colour.colour import colour_create

from sql.generate.language.adjective.adjective_connotation.adjective_connotation import adjective_connotation_create

from sql.generate.language.adjective.adjective import adjective_create

from sql.generate.language.adjective.colour_adjective.colour_adjective import colour_adjective_create

from sql.generate.language.adjective.element_adjective.element_adjective import element_adjective_create


from sql.generate.item.item import item_create

from sql.generate.item.item_diet.item_diet import item_diet_create

from sql.generate.item.item_diet.item_diet_consume.item_diet_consume import item_diet_consume_create


from sql.generate.element.element_effectiveness.element_effectiveness import element_effectiveness_create

from sql.generate.element.element_effectiveness.element_effectiveness_type.element_effectiveness_type import element_effectiveness_type_create

from sql.generate.element.element import element_create

from sql.generate.element.element_type.element_type import element_type_create


from sql.generate.move.move_type.move_type import move_type_create

from sql.generate.move.move_category.move_category import move_category_create

from sql.generate.move.move import move_create


from sql.generate.species.species_family.species_family import species_family_create

from sql.generate.species.species_type.species_type import species_type_create

from sql.generate.species.species import species_create

from sql.generate.moveset.moveset_chance.moveset_chance import moveset_chance_create

from sql.generate.moveset.species_moveset import species_moveset_create

from sql.generate.language.name.person_name.person_name_gender.person_name_gender import person_name_gender_create

from sql.generate.language.name.person_name.person_name_category.person_name_category import person_name_category_create

from sql.generate.language.name.person_name.person_name import person_name_create

from sql.generate.language.name.name_origin.name_origin import name_origin_create

from sql.generate.language.name.name_place.name_place import name_place_create


def panda(connection, table_name) -> pd.DataFrame:
    query = "SELECT * FROM vw_" + table_name
    return pd.read_sql_query(query, connection)

def main() -> int:
    try:
        # make connection to sqlite3
        connection = sqlite3.connect("taverner.db")

        #print the number of database rows that have been changed by connection
        # (for testing. no changes have been made yet so should be 0)
        sql_change_print(connection)

        # make a pointer to issue sql statements to database
        cursor = connection.cursor()
        
        create_func_list = [
            (colour_darkness_create, "colour_darkness"),
            (colour_create, "colour"),
            (adjective_connotation_create, "adjective_connotation"),
            (adjective_create, "adjective"),
            (colour_adjective_create, "colour_adjective"),
            (element_adjective_create, "element_adjective"),
            (item_diet_consume_create, "item_diet_consume"),
            (item_diet_create, "item_diet"),
            (element_type_create, "element_type"),
            (element_create, "element"),
            (item_create, "item"),
            (element_effectiveness_type_create, "element_effectiveness_type"),
            (element_effectiveness_create, "element_effectiveness"),
            (move_type_create, "move_type"),
            (move_category_create, "move_category"),
            (move_create, "move"),
            (species_family_create, "species_family"),
            (species_type_create, "species_type"),
            (species_create, "species"),
            (moveset_chance_create, "moveset_chance"),
            (species_moveset_create, "species_moveset"),
            (person_name_gender_create, "person_name_gender"),
            (person_name_category_create, "person_name_category"),
            (person_name_create, "person_name"),
            (name_origin_create, "name_origin"),
            (name_place_create, "name_place")
        ]

        for create_func, table_name in create_func_list:
            try:
                create_func(connection, cursor)
            except Exception as e:
                print(f"ERROR: table create {table_name}: {e}")
                continue  # Proceed to the next table

        sql_change_print(connection)
    
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
        return 1


    finally:
        # Ensure that resources are properly closed
        if cursor:
            cursor.close()
        if connection:
            connection.close()
 
    return 0

if __name__ == "__main__":
    sys.exit(main())
