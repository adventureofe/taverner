from sql.generate.element.element_type.element_type_list import element_type_list

def sql_table_drop(cursor, table_name): cursor.execute(f"DROP TABLE IF EXISTS {table_name}")

def element_type_create(connection, cursor):
    # overwrite existing table if it already exists
    sql_table_drop(cursor, "element_type")

    # create colour table
    cursor.execute('''CREATE TABLE element_type
(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
)''')

    cursor.executemany("INSERT INTO element_type(name) VALUES (?)", [(name,) for name in element_type_list])

    cursor.execute("DROP VIEW IF EXISTS vw_element_type")

    cursor.execute('''
    CREATE VIEW vw_element_type AS
    SELECT
       et.id AS id,
       et.name AS name
    FROM element_type as et
''')

    # make changes permanent
    connection.commit()
