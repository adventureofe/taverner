import sys
import sqlite3
import pandas as pd
from two_axis_bar_chart import two_axis_bar_chart

def main() -> int:
    # Connect to SQLite database
    connection = sqlite3.connect("../../../taverner.db")

    query = """
    SELECT mc.name AS move_category, COALESCE(COUNT(m.id), 0) AS move_count
    FROM move_category AS mc
    LEFT JOIN move AS m ON mc.id = m.category
    GROUP BY mc.name
    ORDER BY move_count DESC
    """
   

    # Fetch data
    df = pd.read_sql_query(query, connection)

    two_axis_bar_chart(df['move_category'], df['move_count'], "how many moves per move category", "move categories", "number of moves per move category")

    return 0

if __name__ == "__main__":
    main()
