import sys
import sqlite3
import pandas as pd

from sql.generate.colour.colour_main.colour import colour_create
from sql.generate.colour.colour_adjective.colour_adjective import colour_adjective_create
from sql.generate.colour.colour_adjective.colour_adjective_fill.colour_adjective_fill import colour_adjective_fill_create
# from sql.generate.item.item_diet.item_diet import item_diet_create
from sql.generate.item.item_diet.item_consumability.item_consumability import item_consumability_create

def sql_table_drop(cursor, table_name): cursor.execute(f"DRO TABLE IF EXISTS {table_name}")
def sql_table_print(cursor, table_name): print(cursor.execute(f"SELECT * FROM {table_name}").fetchall())
def sql_change_print(connection): print(f"(total connection changes)=>{connection.total_changes}", end='\n')

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
    df_colour = pd.read_sql_query('SELECT * FROM colour', connection)
    print(df_colour)

    
    colour_adjective_create(connection, cursor)
    df_colour_adjective = pd.read_sql_query('SELECT * FROM colour_adjective', connection)
    print(df_colour_adjective)

    
    colour_adjective_fill_create(connection, cursor)
    df_colour_adjective_fill = pd.read_sql_query('SELECT * FROM vw_colour_adjective_fill', connection)
    print(df_colour_adjective_fill)

    '''
    item_diet_create(connection, cursor)
    df_item_diet = pd.read_sql_query('SELECT * FROM item_diet', connection)
    print(df_item_diet)
    '''

    item_consumability_create(connection, cursor)
    df_item_consumability = pd.read_sql_query('SELECT * FROM item_consumability', connection)
    print(df_item_consumability)
    
    sql_change_print(connection)
    cursor.close()
    connection.close()
    return 0

if __name__ == "__main__":
    sys.exit(main())
