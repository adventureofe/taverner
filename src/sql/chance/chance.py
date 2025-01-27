from src.sql.sql_table import base_table_create

from src.sql.chance.chance_list import chance_list as values

def chance_create(
        connection,
        cursor,
        name="chance",
        values=values):
    return base_table_create(connection, cursor, name, values)
