from src.sql.sql_table import base_table_create

from src.sql.species_family.species_family_list import species_family_list as values

def species_family_create(
        connection,
        cursor,
        name="species_family",
        values=values):
    return base_table_create(connection, cursor, name, values)
