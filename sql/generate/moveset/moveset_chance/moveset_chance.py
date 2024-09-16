from sql.generate.moveset.moveset_chance.moveset_chance_list import moveset_chance_list

from sql.utility.sql_table_funcs import sql_table_drop, sql_table_print

def moveset_chance_create(connection, cursor):
    table_name = "moveset_chance"
    list_name = moveset_chance_list

    print("moveset_chance_create DEBUG")
    
    # overwrite existing table if it already exists
    sql_table_drop(cursor, table_name)

    # create colour table
    cursor.execute(f'''CREATE TABLE {table_name} 
(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL CHECK(length(name) <= 128)
)''')

    moveset_chance_tuples = [(value,) for value in list_name]

    cursor.executemany(f"INSERT INTO {table_name}(name) VALUES (?)", moveset_chance_tuples)

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
