from src.sql.sql_table import base_table_create

from src.sql.colour_attr.colour_attr_list import colour_attr_list as values

def colour_attr_create(
        connection,
        cursor,
        name="colour_attr",
        values=values):
    return base_table_create(connection, cursor, name, values)
