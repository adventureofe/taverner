from sql.generate.move.move_category.move_category_list import move_category_list

from sql.utility.sql_table_funcs import sql_table_drop, sql_table_print

def move_category_create(connection, cursor):
    table_name = "move_category"
    list_name = move_category_list
    
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
