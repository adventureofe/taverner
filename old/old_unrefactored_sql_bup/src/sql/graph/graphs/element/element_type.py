import sys
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from two_axis_bar_chart import two_axis_bar_chart


def sql_table_drop(cursor, table_name): cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
def sql_table_print(cursor, table_name): print(cursor.execute(f"SELECT * FROM {table_name}").fetchall())
def sql_change_print(connection): print(f"(total connection changes)=>{connection.total_changes}", end='\n')

def panda(connection, table_name):
    query = "SELECT * FROM vw_" + table_name
    return pd.read_sql_query(query, connection)


def main() -> int:
    # make connection to sqlite3
    connection = sqlite3.connect("../../../taverner.db")

    #print the number of database rows that have been changed by connection
    # (for testing. no changes have been made yet so should be 0)
    sql_change_print(connection)

    query = """
    SELECT element_type, COUNT(*) AS count
    FROM vw_element
    GROUP BY element_type
    """

    df = pd.read_sql_query(query, connection)
 
    two_axis_bar_chart(df['element_type'], df['count'], "number each kind of element type", "element types", "number of each element type", True)


    return 0

if __name__ == "__main__":
    sys.exit(main())