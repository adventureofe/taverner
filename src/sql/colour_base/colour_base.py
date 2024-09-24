from src.sql.sql_table import base_table_create

from src.sql.colour_base.colour_base_list import colour_base_list

def colour_base_create(
        connection,
        cursor,
        name="colour_base",
        values=colour_base_list):
    return base_table_create(connection, cursor, name, values)
