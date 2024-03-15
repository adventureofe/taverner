import sys
import sqlite3
import pandas as pd

from sql.generate.language.adjective.colour_adjective.colour_adjective_list import colour_adjective_list


def sql_table_drop(cursor, table_name): cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
def sql_table_print(cursor, table_name): print(cursor.execute(f"SELECT * FROM {table_name}").fetchall())

def colour_adjective_create(connection, cursor):
    # overwrite existing table if it already exists
    sql_table_drop(cursor, "colour_adjective")

    # create colour table
    cursor.execute('''
CREATE TABLE colour_adjective
(
    id INTEGER PRIMARY KEY,
    adjective INTEGER NOT NULL,
    colour INTEGER NOT NULL
    
)''')

    

    cursor.executemany("INSERT INTO colour_adjective(adjective, colour) VALUES(?, ? )", colour_adjective_list)

    cursor.execute("DROP VIEW IF EXISTS vw_colour_adjective")

    cursor.execute('''
CREATE VIEW vw_colour_adjective AS
SELECT
    ca.id as id,
    ca.colour as cid,
    c.name as colour,
    ca.adjective as aid,
    a.name as adjective
FROM colour_adjective AS ca
INNER JOIN colour AS c ON cid = c.id
INNER JOIN adjective AS a ON aid = ca.id;
''')

    # make changes permanent
    connection.commit()


