from sql.generate.species.species_list import species_list

def sql_table_drop(cursor, table_name): cursor.execute(f"DROP TABLE IF EXISTS {table_name}")

def species_create(connection, cursor):
    # overwrite existing table if it already exists
    sql_table_drop(cursor, "species")

    # create colour table
    cursor.execute('''CREATE TABLE species 
(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    colour INTEGER NOT NULL
)''')

    cursor.executemany("INSERT INTO species(name, colour) VALUES (?, ?)", list(species_list))

    cursor.execute("DROP VIEW IF EXISTS vw_species")

    cursor.execute('''
    CREATE VIEW vw_species AS
    SELECT
       s.id AS id,
       s.name AS name,
       c.id AS cid,
       c.name AS colour
    FROM species AS s
    INNER JOIN colour AS c ON e.colour = c.id
''')

    # make changes permanent
    connection.commit()
