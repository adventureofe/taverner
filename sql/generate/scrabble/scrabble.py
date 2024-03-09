import sys
import sqlite3
import pandas as pd

sql_table_drop = lambda cursor, table_name: cursor.execute(f"DROP TABLE IF EXISTS {table_name}")

from sql.generate.scrabble.scrabble_list import scrabble_list

def scrabble_create(connection, cursor):
    # overwrite existing table if it already exists
    sql_table_drop(cursor, "scrabble")

    cursor.execute("CREATE TABLE scrabble (id INTEGER PRIMARY KEY, letter TEXT NOT NULL, english_value INTEGER NOT NULL, english_quantity INTEGER NOT NULL, afrikaans_value INTEGER NOT NULL, afrikaans_quantity INTEGER NOT NULL, german_value INTEGER NOT NULL, german_quantity INTEGER NOT NULL, latin_value INTEGER NOT NULL, latin_quantity INTEGER NOT NULL, irish_value INTEGER NOT NULL, irish_quantity INTEGER NOT NULL, polish_value INTEGER NOT NULL, polish_quantity INTEGER NOT NULL, portuguese_value INTEGER NOT NULL, portuguese_quantity INTEGER NOT NULL, is_vowel BOOLEAN NOT NULL, double_start BOOLEAN NOT NULL, double_mid BOOLEAN NOT NULL, double_end BOOLEAN NOT NULL)")

    cursor.executemany("INSERT INTO scrabble(letter, english_value, english_quantity, afrikaans_value, afrikaans_quantity, german_value, german_quantity, latin_value, latin_quantity, irish_value, irish_quantity, polish_value, polish_quantity, portuguese_value, portuguese_quantity,  is_vowel, double_start, double_mid, double_end) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", list(scrabble_list))

    # make changes permanent
    connection.commit()
