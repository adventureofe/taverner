import sys
import sqlite3
import pandas as pd

from sql.generate.element.element_effectiveness.element_effectiveness_list import element_effectiveness_list

def sql_table_drop(cursor, table_name): cursor.execute(f"DROP TABLE IF EXISTS {table_name}")

def element_effectiveness_create(connection, cursor):
    # overwrite existing table if it already exists
    sql_table_drop(cursor, "element_effectiveness")

    # create table
    cursor.execute('''CREATE TABLE element_effectiveness
    (
    id INTEGER PRIMARY KEY,
    attacker INTEGER NOT NULL,
    defender INTEGER NOT NULL,
    effectiveness INTEGER NOT NULL,
    FOREIGN KEY (attacker) REFERENCES element(id),
    FOREIGN KEY (defender) REFERENCES element(id)
    )''')

    #insert values into table
    cursor.executemany("INSERT INTO element_effectiveness(attacker, defender, effectiveness) VALUES (?, ?, ?)", element_effectiveness_list)

    #overwrite existing table if it already exists
    cursor.execute('DROP VIEW IF EXISTS vw_element_effectiveness')

    #create view for table
    cursor.execute('''
CREATE VIEW vw_element_effectiveness AS
SELECT
    ef.attacker AS atk,
    e1.name AS attacker,
    ef.defender AS def,
    e2.name AS defender,
    et.level AS eff,
    et.name AS effectiveness
FROM element_effectiveness AS ef
INNER JOIN element AS e1 ON ef.attacker = e1.id
INNER JOIN element AS e2 ON ef.defender = e2.id
INNER JOIN element_effectiveness_type AS et ON et.id = ef.effectiveness;
    ''')


    # make changes permanent
    connection.commit()
