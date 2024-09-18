import sys
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


from src.util.sql_util import sql_table_drop, sql_table_print, sql_change_print, sql_to_df, sql_add_funcs

from src.sql.create.sql_create_all import sql_create_all 

def main() -> int:
    try:
        # make connection to sqlite3
        connection = sqlite3.connect("taverner.db")

        #print the number of database rows that have been changed by connection
        # (for testing. no changes have been made yet so should be 0)
        sql_change_print(connection)

        # make a pointer to issue sql statements to database
        cursor = connection.cursor()

        sql_create_all(connection, cursor)

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
