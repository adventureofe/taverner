from src.sql.sql_table import base_table_create

from src.sql.move_category.move_category_list import move_category_list as values

def move_category_create(
        connection,
        cursor,
        name="move_category",
        values=values):
    return base_table_create(connection, cursor, name, values)
