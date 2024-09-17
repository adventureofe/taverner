import sys
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

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
        SELECT attacker,
           SUM(CASE WHEN effectiveness = 'very weak' THEN 1 ELSE 0 END) AS very_weak_count,
           SUM(CASE WHEN effectiveness = 'weak' THEN 1 ELSE 0 END) AS weak_count,
           SUM(CASE WHEN effectiveness = 'somewhat weak' THEN 1 ELSE 0 END) AS somewhat_weak_count,
           SUM(CASE WHEN effectiveness = 'neutral' THEN 1 ELSE 0 END) AS neutral_count,
           SUM(CASE WHEN effectiveness = 'somewhat strong' THEN 1 ELSE 0 END) AS somewhat_strong_count,
           SUM(CASE WHEN effectiveness = 'strong' THEN 1 ELSE 0 END) AS strong_count,
           SUM(CASE WHEN effectiveness = 'very strong' THEN 1 ELSE 0 END) AS very_strong_count
    FROM vw_element_effectiveness
    GROUP BY attacker
    ORDER BY attacker;
    """

    df = pd.read_sql_query(query, connection)
# Set up the plot
    fig, ax = plt.subplots(figsize=(10, 7))
    
    # Plot each effectiveness type
    effectiveness_types = ['very_weak_count', 'weak_count', 'somewhat_weak_count', 'neutral_count', 'somewhat_strong_count', 'strong_count', 'very_strong_count']
    colors = ['red', 'orange', "yellow", 'gray', "blue", 'cyan', 'green']  # Color for each effectiveness type

    # Stack bars
    df.set_index('attacker')[effectiveness_types].plot(kind='bar', stacked=True, color=colors, ax=ax)
    
    # Customize the plot
    ax.set_title('Effectiveness Count by Attacker')
    ax.set_xlabel('Attacker')
    ax.set_ylabel('Count')
    ax.legend(title='Effectiveness', labels=['Weak', 'Somewhat Weak', 'Neutral', 'Strong', 'Very Strong'])
    ax.set_xticks(range(len(df['attacker'])))
    ax.set_xticklabels(df['attacker'], rotation=45, ha='right')

    # Set background color
    ax.set_facecolor('black')
    fig.patch.set_facecolor('black')
    
    # Set grid and text color
    ax.yaxis.grid(True, linestyle='--', color='green')
    ax.xaxis.grid(False)
    ax.tick_params(axis='both', colors='green')
    ax.spines['top'].set_color('green')
    ax.spines['right'].set_color('green')
    ax.spines['left'].set_color('green')
    ax.spines['bottom'].set_color('green')
    
    plt.tight_layout()
    plt.show()

    return 0

if __name__ == "__main__":
    sys.exit(main())
