import sys
import sqlite3
import pandas as pd


from sql.generate.place.endinr_list import ending_list

sql_table_drop = lambda cursor, table_name: cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
sql_table_print = lambda cursor, table_name: print(cursor.execute(f"SELECT * FROM {table_name}").fetchall())

def colour_create(connection, cursor):
    # overwrite existing table if it already exists
    sql_table_drop(cursor, "ending")

    # create colour table
    cursor.execute("CREATE TABLE ending ( id INTEGER PRIMARY KEY, name TEXT NOT NULL, geography TEXT NOT NULL, region TEXT NOT NULL, syllable INTEGER NOT NULL)")

    cursor.executemany("INSERT INTO ending(name, geography, region, syllable) VALUES (?, ?, ?)", list(ending_list))

    # make changes permanent
    connection.commit()
