from sql.generate.species.species_list import species_list

def sql_table_drop(cursor, table_name): cursor.execute(f"DROP TABLE IF EXISTS {table_name}")

def species_create(connection, cursor):
    table_name = "species"
    list_name = species_list
    
    # overwrite existing table if it already exists
    sql_table_drop(cursor, table_name)

    # create colour table
    cursor.execute(f'''CREATE TABLE {table_name} 
(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL CHECK(length(name) <= 128),
    colour INTEGER NOT NULL
)''')

    cursor.executemany(f"INSERT INTO {table_name}(name, colour) VALUES (?, ?)", list(list_name))

    cursor.execute(f"DROP VIEW IF EXISTS vw_{table_name}")

    cursor.execute(f'''
    CREATE VIEW vw_{table_name} AS
    SELECT
       tn.id AS id,
       tn.name AS name,
       c.id AS cid,
       c.name AS colour
    FROM {table_name} AS tn
    INNER JOIN colour AS c ON tn.colour = c.id
''')

    # make changes permanent
    connection.commit()
