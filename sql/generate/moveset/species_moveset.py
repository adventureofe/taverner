import sys
import sqlite3
import pandas as pd

from sql.generate.species_moveset.species_moveset_list import species_moveset_list

def sql_table_drop(cursor, table_name): cursor.execute(f"DROP TABLE IF EXISTS {table_name}")


def move_create(connection, cursor):
    table_name = "species_moveset"
    list_name = species_moveset_list

    # overwrite existing table if it already exists
    sql_table_drop(cursor, table_name)

    # create table
    cursor.execute(f'''CREATE TABLE {table_name}
(
        species INTEGER NOT NULL,
        move INTEGER NOT NULL,
        level INTEGER NOT NULL,
        chance INTEGER NOT NULL,
        PRIMARY KEY (species, move),
        FOREIGN KEY (species) REFERENCES species(id),
        FOREIGN KEY (move) REFERENCES move(id),
        FOREIGN KEY (change) REFERENCES moveset_chance(id)
)''')

    #insert values into table
    cursor.executemany(f"INSERT INTO {table_name}(species, move, level, chance, ) VALUES (?, ?, ?, ?)", list(list_name))

    #overwrite existing table if it already exists
    cursor.execute(f'DROP VIEW IF EXISTS vw_{table_name}')

    #create view for table
    cursor.execute(f'''
    CREATE VIEW vw_{table_name} AS
    SELECT
        sm.species AS species_id,
        sp.name AS species_name,
        sm.move AS move_id,
        mv.name AS move_name,
        sm.level AS level,
        sm.chance AS chance
    FROM {table_name} AS sm
    INNER JOIN species AS sp ON sm.species = sp.id
    INNER JOIN move AS mv ON sm.move = mv.id
''')

    # make changes permanent
    connection.commit()
