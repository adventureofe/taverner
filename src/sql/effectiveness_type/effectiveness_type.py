from src.sql.sql_table import base_table_create

from src.sql.effectiveness_type.effectiveness_type_list import effectiveness_type_list as values

def effectiveness_type_create(
        connection,
        cursor,
        name="effectiveness_type",
        values=values):
    return base_table_create(connection, cursor, name, values)
