import sys
import sqlite3
import pandas as pd

from sql.generate.language.adjective.colour_adjective.colour_adjective_list import colour_adjective_list


def sql_table_drop(cursor, table_name): cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
def sql_table_print(cursor, table_name): print(cursor.execute(f"SELECT * FROM {table_name}").fetchall())

def colour_adjective_create(connection, cursor):
    table_name = "colour_adjective"
    list_name = colour_adjective_list
    
    # overwrite existing table if it already exists
    sql_table_drop(cursor, table_name)

    # create colour table
    cursor.execute(f'''
CREATE TABLE {table_name}
(
    id INTEGER PRIMARY KEY,
    adjective INTEGER NOT NULL,
    colour INTEGER NOT NULL
    
)''')

    

    cursor.executemany(f"INSERT INTO {table_name}(adjective, colour) VALUES(?, ? )", list_name)

    cursor.execute(f"DROP VIEW IF EXISTS vw_{table_name}")

    cursor.execute(f'''
CREATE VIEW vw_{table_name} AS
SELECT
    tn.id as id,
    tn.colour as cid,
    c.name as colour,
    tn.adjective as aid,
    a.name as adjective
FROM {table_name} AS tn
INNER JOIN colour AS c ON cid = c.id
INNER JOIN adjective AS a ON aid = a.id;
''')

    # make changes permanent
    connection.commit()


