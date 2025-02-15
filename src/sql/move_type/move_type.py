from src.sql.sql_table import base_table_create

from src.sql.move_type.move_type_list import move_type_list as values

def move_type_create(
        connection,
        cursor,
        name="move_type",
        values=values):
    return base_table_create(connection, cursor, name, values)
