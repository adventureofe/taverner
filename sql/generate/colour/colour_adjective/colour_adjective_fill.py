import sys
import sqlite3
import pandas as pd

from sql.generate.colour.colour_adjective.colour_adjective_fill_list import colour_adjective_fill_list

sql_table_drop = lambda cursor, table_name: cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
sql_table_print = lambda cursor, table_name: print(cursor.execute(f"SELECT * FROM {table_name}").fetchall())

def colour_adjective_fill_create(connection, cursor):
    # overwrite existing table if it already exists
    sql_table_drop(cursor, "colour_adjective_fill")

    # create colour table
    cursor.execute('''
CREATE TABLE colour_adjective_fill
(
    id INTEGER PRIMARY KEY,
    adjective INTEGER NOT NULL,
    colour INTEGER NOT NULL
    
)''')

    

    cursor.executemany("INSERT INTO colour_adjective_fill(adjective, colour) VALUES(?, ? )", colour_adjective_fill_list)

    cursor.execute("DROP VIEW IF EXISTS vw_colour_adjective_fill")

    cursor.execute('''
CREATE VIEW vw_colour_adjective_fill AS
SELECT
    caf.id as id,
    caf.colour as colour_id,
    c.name as colour_name,
    caf.adjective as adjective_id,
    ca.name as adjective_name
FROM colour_adjective_fill AS caf
INNER JOIN colour AS c ON colour_id = c.id
INNER JOIN colour_adjective AS ca ON adjective_id = ca.id;
''')


    # make changes permanent
    connection.commit()


