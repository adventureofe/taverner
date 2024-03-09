import sys
import sqlite3
import pandas as pd

from sql.generate.colour.colour import colour_create
from sql.generate.colour.colour_adjective.colour_adjective import colour_adjective_create
from sql.generate.colour.colour_adjective.colour_adjective_fill import colour_adjective_fill_create

def sql_table_drop(): lambda cursor, table_name: cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
def sql_table_print(): lambda cursor, table_name: print(cursor.execute(f"SELECT * FROM {table_name}").fetchall())

def sql_change_print(): lambda connection : print(f"(total connection changes)=>{connection.total_changes}", end='\n')


def main() -> int:
    # make connection to sqlite3
    connection = sqlite3.connect("taverner.db")

    #print the number of database rows that have been changed by connection
    # (for testing. no changes have been made yet so should be 0)
    sql_change_print(connection)

    # make a pointer to issue sql statements to database
    cursor = connection.cursor()

    #scrabble_create(connection, cursor)
    #df_scrabble = pd.read_sql_query('SELECT * FROM scrabble', connection)
    #print(df_scrabble)
    #filtered_df = df_scrabble[(df_scrabble["irish_quantity"] != 0) & (df_scrabble["portuguese_quantity"]  != 0)][['letter', 'english_value', 'english_quantity', 'irish_value', 'irish_quantity']]
    #print(filtered_df)
    #vowels = df_scrabble[df_scrabble['is_vowel'] == True][['letter', 'english_quantity', 'english_value']]
    #print(sum(vowels['english_quantity']))
    # roll_dice(1, 20, 3)


    # get PANDAS dataframe
    colour_create(connection, cursor)
    df_colour = pd.read_sql_query('SELECT * FROM colour', connection)
    print(df_colour)

    colour_adjective_create(connection, cursor)
    df_colour_adjective = pd.read_sql_query('SELECT * FROM colour_adjective', connection)
    print(df_colour_adjective)

    colour_adjective_fill_create(connection, cursor)
    df_colour_adjective_fill = pd.read_sql_query('SELECT * FROM colour_adjective_fill', connection)
    print(df_colour_adjective_fill)

    sql_change_print(connection)
    cursor.close()
    connection.close()
    return 0

if __name__ == "__main__":
    sys.exit(main())
