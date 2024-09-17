import sys
import sqlite3
import pandas as pd
from two_axis_bar_chart import two_axis_bar_chart

def main() -> int:
    # Connect to SQLite database
    connection = sqlite3.connect("../../../taverner.db")

    query = """
    SELECT st.name AS species_type, COALESCE(COUNT(s.id), 0) AS species_count
    FROM species_type AS st
    LEFT JOIN species AS s ON st.id = s.species_type
    GROUP BY st.name
    ORDER BY species_count DESC
    """
   

    # Fetch data
    df = pd.read_sql_query(query, connection)

    two_axis_bar_chart(df['species_type'], df['species_count'], "how many species per species type", "species types", "number of species per species type")

    return 0

if __name__ == "__main__":
    main()
