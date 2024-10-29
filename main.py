import sys
import sqlite3
import pandas as pd
from src.sql.sql_table import SQLTable

from src.sql.colour.colour import colour_create
from src.sql.colour_darkness.colour_darkness import colour_darkness_create
from src.sql.colour_base.colour_base import colour_base_create

from src.sql.element.element import element_create
from src.sql.move_type.move_type import move_type_create
from src.sql.move_category.move_category import move_category_create
from src.sql.move.move import move_create

def main() -> int:
    try:
        connection = sqlite3.connect("taverner.db")
        cursor = connection.cursor()

        colour_create(connection, cursor)
        colour_darkness_create(connection, cursor)
        colour_base_create(connection, cursor)

        element_create(connection, cursor)
        move_type_create(connection, cursor)
        move_category_create(connection, cursor)
        move_create(connection, cursor)

        # make changes permanent
        connection.commit()

    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
        return 1

    finally:
        # Ensure that resources are properly closed
        if cursor:
            cursor.close()
        if connection:
            connection.close()

    return 0

if __name__ == "__main__":
    sys.exit(main())
