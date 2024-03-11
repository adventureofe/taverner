

from sql.generate.element.element_main.element_list import element_list

def sql_table_drop(cursor, table_name): cursor.execute(f"DROP TABLE IF EXISTS {table_name}")

def colour_create(connection, cursor):
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

    # make changes permanen
    
    connection.commit()
