import sys
import sqlite3
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from two_axis_bar_chart import two_axis_bar_chart

def sql_table_drop(cursor, table_name): cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
def sql_table_print(cursor, table_name): print(cursor.execute(f"SELECT * FROM {table_name}").fetchall())
def sql_change_print(connection): print(f"(total connection changes)=>{connection.total_changes}", end='\n')

def panda(connection, table_name):
    query = "SELECT * FROM vw_" + table_name
    return pd.read_sql_query(query, connection)

def make_bar_graph(x_axis, y_axis):
    green_color = "#00FF00"
    fig, ax = plt.subplots(figsize=(2, 2), facecolor='black',
                       layout='constrained')
    fig.suptitle('Figure')
    ax.set_title('Axes', color=green_color, loc='left', fontstyle='oblique', fontsize='xx-large')
    ax.set_xlabel('X Axis', color=green_color)
    ax.set_ylabel('Y Axis', color=green_color)
    ax.tick_params(axis='x', colors=green_color, rotation=45)  
    ax.tick_params(axis='y', colors=green_color)  
    ax.yaxis.set_major_locator(MultipleLocator(1))
    plt.grid(True, color=green_color, linestyle="--", linewidth=0.5)

    # Set background colors (optional)
    ax.set_facecolor('black')                     # Axes background
    fig.patch.set_facecolor('black')              # Figure background

    ax.spines['left'].set_color(green_color)
    ax.spines['bottom'].set_color(green_color)

    plt.show()


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
    """

    df = pd.read_sql_query(query, connection)

    two_axis_bar_chart(df["element"], df["very_weak_count"], "count_element_effectiveness_very_weak", "element", "count of very weak effectiveness")
 

    return 0

if __name__ == "__main__":
    sys.exit(main())
