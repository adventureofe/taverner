from src.sql.sql_table import base_table_create

from src.sql.colour_base.colour_base_list import colour_base_list as values

def colour_base_create(
        connection,
        cursor,
        name="colour_base",
        values=values):
    return base_table_create(connection, cursor, name, values)
