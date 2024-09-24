import sqlite3

def count_entries():
    # Connect to the SQLite database
    connection = sqlite3.connect("../../taverner.db")
    cursor = connection.cursor()

    # List of tables to check
    tables = [
        "adjective",
        "adjective_connotation",
        "colour",
        "colour_adjective",
        "element",
        "element_effectiveness",
        "element_effectiveness_type",
        "element_type",
        "item",
        "item_diet",
        "item_diet_consume",
        "move",
        "move_category",
        "move_type",
        "species",
        "species_type",
        "species_family",
    ]

    print("Table Entry Counts:")
    for table in tables:
        # Execute the SQL query to count rows
        cursor.execute(f"SELECT COUNT(*) FROM {table}")
        count = cursor.fetchone()[0]
        print(f"{table}: {count}")

    # Close the connection
    connection.close()

if __name__ == "__main__":
    count_entries()
