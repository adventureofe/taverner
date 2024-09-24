import sys
import sqlite3
import pandas as pd
from two_axis_bar_chart import two_axis_bar_chart

def main() -> int:
    # Connect to SQLite database
    connection = sqlite3.connect("../../../taverner.db")

    query = """
    SELECT e.name AS element, COALESCE(COUNT(m.id), 0) AS move_count
    FROM element AS e
    LEFT JOIN move AS m ON e.id = m.element
    GROUP BY e.name
    ORDER BY move_count DESC
    """
   

    # Fetch data
    df = pd.read_sql_query(query, connection)

    two_axis_bar_chart(df['element'], df['move_count'], "how many moves per element", "elements", "number of moves per element", True)

    return 0

if __name__ == "__main__":
    main()
