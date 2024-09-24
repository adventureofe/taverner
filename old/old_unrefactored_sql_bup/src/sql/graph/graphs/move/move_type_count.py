import sys
import sqlite3
import pandas as pd
from two_axis_bar_chart import two_axis_bar_chart

def main() -> int:
    # Connect to SQLite database
    connection = sqlite3.connect("../../../taverner.db")

    query = """
    SELECT mt.name AS move_type, COALESCE(COUNT(m.id), 0) AS move_count
    FROM move_type AS mt
    LEFT JOIN move AS m ON mt.id = m.type
    GROUP BY mt.name
    ORDER BY move_count DESC
    """
   

    # Fetch data
    df = pd.read_sql_query(query, connection)

    two_axis_bar_chart(df['move_type'], df['move_count'], "how many moves per move type", "move types", "number of moves per move type")

    return 0

if __name__ == "__main__":
    main()
