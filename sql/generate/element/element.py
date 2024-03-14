from sql.generate.element.element_list import element_list

def sql_table_drop(cursor, table_name): cursor.execute(f"DROP TABLE IF EXISTS {table_name}")

def element_create(connection, cursor):
    # overwrite existing table if it already exists
    sql_table_drop(cursor, "element")

    # create colour table
    cursor.execute('''CREATE TABLE element 
(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    colour INTEGER NOT NULL
)''')

    cursor.executemany("INSERT INTO element(name, colour) VALUES (?, ?)", list(element_list))

    cursor.execute("DROP VIEW IF EXISTS vw_element")

    cursor.execute('''
    CREATE VIEW vw_element AS
    SELECT
       e.id AS id,
       e.name AS name,
       c.id AS colour_id,
       c.name AS colour
    FROM element as e
    INNER JOIN colour AS c ON e.colour = c.id
''')

    # make changes permanent
    connection.commit()
