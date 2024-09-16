import sys
import sqlite3
import pandas as pd
from sql.utility.sql_table_funcs import sql_table_drop, sql_table_print

from sql.generate.language.adjective.element_adjective.element_adjective_list import element_adjective_list

def element_adjective_create(connection, cursor):
    table_name = "element_adjective"
    list_name = element_adjective_list
    
    # overwrite existing table if it already exists
    sql_table_drop(cursor, table_name)

    # create colour table
    cursor.execute(f'''
CREATE TABLE {table_name}
(
    id INTEGER PRIMARY KEY,
    adjective INTEGER NOT NULL,
    element INTEGER NOT NULL
    
)''')

    

    cursor.executemany(f"INSERT INTO {table_name}(adjective, element) VALUES(?, ? )", list_name)

    cursor.execute(f"DROP VIEW IF EXISTS vw_{table_name}")

    cursor.execute(f'''
CREATE VIEW vw_{table_name} AS
SELECT
    tn.id as id,
    tn.element as eid,
    e.name as element,
    tn.adjective as aid,
    a.name as adjective
FROM {table_name} AS tn
INNER JOIN element AS e ON eid = e.id
INNER JOIN adjective AS a ON aid = a.id;
''')

    # make changes permanent
    connection.commit()


