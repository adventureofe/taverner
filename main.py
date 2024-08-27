import sys
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

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

def sql_table_drop(cursor, table_name): cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
def sql_table_print(cursor, table_name): print(cursor.execute(f"SELECT * FROM {table_name}").fetchall())
def sql_change_print(connection): print(f"(total connection changes)=>{connection.total_changes}", end='\n')


def panda(connection, table_name):
    query = "SELECT * FROM vw_" + table_name
    return pd.read_sql_query(query, connection)


def main() -> int:
    # make connection to sqlite3
    connection = sqlite3.connect("taverner.db")

    #print the number of database rows that have been changed by connection
    # (for testing. no changes have been made yet so should be 0)
    sql_change_print(connection)

    # make a pointer to issue sql statements to database
    cursor = connection.cursor()

    colour_darkness_create(connection, cursor)
    df_colour_darkness = panda(connection, "colour_darkness")
    print(df_colour_darkness)

    # get PANDAS dataframe
    colour_create(connection, cursor)
    df_colour = panda(connection, "colour")
    #print(df_colour, end="\n\n")

    adjective_connotation_create(connection, cursor)
    df_adjective_connotation = panda(connection, "adjective_connotation")
    #print(df_adjective_connotation)

    adjective_create(connection, cursor)
    df_adjective = panda(connection, "adjective")
    #print(df_adjective)

    colour_adjective_create(connection, cursor)
    df_colour_adjective = panda(connection, "colour_adjective")
    #print(df_colour_adjective)

    element_adjective_create(connection, cursor)
    df_element_adjective =panda(connection, "element_adjective")
    print(df_element_adjective)

    item_diet_consume_create(connection, cursor)
    df_item_diet_consume = panda(connection, "item_diet_consume")
    # print(df_item_diet_consume)

    item_diet_create(connection, cursor)
    df_item_diet = panda(connection, "item_diet")
    # print(df_item_diet)

    element_type_create(connection, cursor)
    df_element_type = panda(connection, "element_type")
    # print(df_element_type)

    element_create(connection, cursor)
    df_element = panda(connection, "element")
    # print(df_element)

    item_create(connection, cursor)
    df_item = panda(connection, "item")
    # print(df_item)

    element_effectiveness_type_create(connection, cursor)
    df_element_effectiveness_type = panda(connection, "element_effectiveness_type")
    # print(df_element_effectiveness_type)

    element_effectiveness_create(connection, cursor)
    df_element_effectiveness = panda(connection, "element_effectiveness")
    #print(df_element_effectiveness)

    move_type_create(connection, cursor)
    df_move_type = panda(connection, "move_type")
    #print(df_move_type)

    move_category_create(connection, cursor)
    df_move_category = panda(connection, "move_category")
    #print(df_move_category)

    move_create(connection, cursor)
    df_move = panda(connection, "move")
    #print(df_move)

    species_family_create(connection, cursor)
    df_species_family = panda(connection, "species_family")
    #print(df_species_family)

    species_type_create(connection, cursor)
    df_species_type= panda(connection, "species_type")
    #print(df_species_type)

    species_create(connection, cursor)
    df_species= panda(connection, "species")
    #print(df_species)

    moveset_chance_create(connection, cursor)
    df_moveset_chance = panda(connection, "moveset_chance")
    #print(df_moveset_chance)
    
    species_moveset_create(connection, cursor)
    df_species_moveset=panda(connection, "species_moveset")
    #print(df_species_moveset)

    person_name_gender_create(connection, cursor)
    df_person_name_gender=panda(connection, "person_name_gender")
    #print(df_person_name_gender)
    
    person_name_category_create(connection, cursor)
    df_person_name_category=panda(connection, "person_name_category")
    #print(df_person_name_category)

    person_name_create(connection, cursor)
    df_person_name=panda(connection, "person_name")
    #print(df_person_name)
    
    

    sql_change_print(connection)
    cursor.close()
    connection.close()
 
    return 0

if __name__ == "__main__":
    sys.exit(main())
