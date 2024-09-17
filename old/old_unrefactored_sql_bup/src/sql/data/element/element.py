from sql.generate.element.element_list import element_list
from sql.utility.sql_table_funcs import sql_table_drop, sql_table_print

def element_create(connection, cursor):
    table_name = "element"
    list_name = element_list
    
    # overwrite existing table if it already exists
    sql_table_drop(cursor, table_name)

    # create table
    cursor.execute(f'''CREATE TABLE {table_name} 
(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL CHECK(length(name) <= 128),
    colour INTEGER NOT NULL,
    element_type INTEGER NOT NULL,
    FOREIGN KEY (colour) REFERENCES colour(id),
    FOREIGN KEY (element_type) REFERENCES element_type(id) 
)''')

    cursor.executemany(f"INSERT INTO {table_name}(name, colour, element_type) VALUES (?, ?, ?)", list(list_name))

    cursor.execute(f"DROP VIEW IF EXISTS vw_{table_name}")

    cursor.execute(f'''
    CREATE VIEW vw_{table_name} AS
    SELECT
       tn.id AS id,
       tn.name AS name,
       c.id AS cid,
       c.name AS colour,
       et.id AS etid,
       et.name AS element_type
    FROM {table_name} as tn
    INNER JOIN colour AS c ON tn.colour = c.id
    INNER JOIN element_type AS et ON tn.element_type = et.id
''')

    # make changes permanent
    connection.commit()
