import sys
import sqlite3
import pandas as pd

from sql.generate.colour.colour import colour_create


from sql.generate.language.adjective.adjective import adjective_create

from sql.generate.language.adjective.colour_adjective.colour_adjective import colour_adjective_create


from sql.generate.item.item import item_create

from sql.generate.item.item_diet.item_diet import item_diet_create

from sql.generate.item.item_diet.item_diet_consume.item_diet_consume import item_diet_consume_create


from sql.generate.element.element_effectiveness.element_effectiveness import element_effectiveness_create

from sql.generate.element.element_effectiveness.element_effectiveness_type.element_effectiveness_type import element_effectiveness_type_create

from sql.generate.element.element import element_create

from sql.generate.element.element_type.element_type import element_type_create



def sql_table_drop(cursor, table_name): cursor.execute(f"DRO TABLE IF EXISTS {table_name}")
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

    # get PANDAS dataframe
    colour_create(connection, cursor)
    df_colour = panda(connection, "colour")
    print(df_colour, end="\n\n")

    '''
    adjective_create(connection, cursor)
    df_adjective = panda(connection, "adjective")
    # print(df_adjective)

    colour_adjective_create(connection, cursor)
    df_colour_adjective = panda(connection, "colour_adjective")
    # print(df_colour_adjective)

    item_diet_consume_create(connection, cursor)
    df_item_diet_consume = pd.read_sql_query('SELECT * FROM item_diet_consume', connection)
    # print(df_item_diet_consume)

    item_diet_create(connection, cursor)
    df_item_diet = pd.read_sql_query('SELECT * FROM item_diet', connection)
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
    '''

    element_effectiveness_type_create(connection, cursor)
    df_element_effectiveness_type = panda(connection, "element_effectiveness_type")
    print(df_element_effectiveness_type)

    element_effectiveness_create(connection, cursor)
    df_element_effectiveness = pd.read_sql_query('SELECT * FROM element_effectiveness', connection)
    print(df_element_effectiveness)

    sql_change_print(connection)
    cursor.close()
    connection.close()
    return 0

if __name__ == "__main__":
    sys.exit(main())
