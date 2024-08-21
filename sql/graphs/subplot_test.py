import sys
import sqlite3
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

def sql_table_drop(cursor, table_name): cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
def sql_table_print(cursor, table_name): print(cursor.execute(f"SELECT * FROM {table_name}").fetchall())
def sql_change_print(connection): print(f"(total connection changes)=>{connection.total_changes}", end='\n')

def panda(connection, table_name):
    query = "SELECT * FROM vw_" + table_name
    return pd.read_sql_query(query, connection)

def gen_bar_chart():
        fig = plt.figure()

        return 4


def main() -> int:
    # make connection to sqlite3
    connection = sqlite3.connect("../../taverner.db")

    #print the number of database rows that have been changed by connection
    # (for testing. no changes have been made yet so should be 0)
    sql_change_print(connection)

    query = """
    SELECT attacker AS element,
        SUM(CASE WHEN effectiveness = 'very weak' THEN 1 ELSE 0 END) AS very_weak_count
    FROM vw_element_effectiveness
    GROUP BY attacker
    ORDER BY very_weak_count DESC;
    """
    green_color = "#00FF00"

    df = pd.read_sql_query(query, connection)
 
    fig = plt.figure(figsize=(10,6))

    ax = plt.gca()
    ax.set_facecolor('black')
    plt.gcf().set_facecolor('black')
  
    plt.bar(df['element'], df['very_weak_count'], color="red")

    plt.xlabel('Element', color=green_color)
    plt.ylabel('Count', color=green_color)
    plt.title('Count of Very Strong Effectiveness Type', color=green_color)
    plt.xticks(rotation=45, color=green_color)
    plt.yticks(color=green_color)

    ax.yaxis.set_major_locator(MultipleLocator(1))
    plt.grid(True, color=green_color, linestyle="--", linewidth=0.5)


    return 0

if __name__ == "__main__":
    sys.exit(main())
