from sql.generate.species.species_family.species_family_list import species_family_list

from sql.utility.sql_table_funcs import sql_table_drop, sql_table_print

def species_family_create(connection, cursor):
    table_name = "species_family"
    list_name = species_family_list
    
    # overwrite existing table if it already exists
    sql_table_drop(cursor, table_name)

    # create colour table
    cursor.execute(f'''CREATE TABLE {table_name} 
(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL CHECK(length(name) <= 128)
)''')

    cursor.executemany(f"INSERT INTO {table_name}(name) VALUES (?)", [(name,) for name in list_name])

    cursor.execute(f"DROP VIEW IF EXISTS vw_{table_name}")

    cursor.execute(f'''
    CREATE VIEW vw_{table_name} AS
    SELECT
       tn.id AS id,
       tn.name AS name
    FROM {table_name} as tn
''')

    # make changes permanent
    connection.commit()
