from sql.generate.species.species_list import species_list
from sql.utility.sql_table_funcs import sql_table_drop, sql_table_print

def species_create(connection, cursor):
    table_name = "species"
    list_name = species_list
    
    # overwrite existing table if it already exists
    sql_table_drop(cursor, table_name)

    # create colour table
    cursor.execute(f'''CREATE TABLE {table_name} 
(
    id INTEGER PRIMARY KEY,
    species_family INTEGER NOT NULL,
    species_type INTEGER NOT NULL,
    name TEXT NOT NULL CHECK(length(name) <= 128),
    colour_primary INTEGER NOT NULL,
    colour_secondary INTEGER NOT NULL,
    height_min INTEGER NOT NULL,
    height_max INTEGER NOT NULL,
    weight_min INTEGER NOT NULL,
    weight_max INTEGER NOT NULL,
    FOREIGN KEY(species_family) REFERENCES species_family(id),
    FOREIGN KEY(species_type) REFERENCES species_type(id),
    FOREIGN KEY(colour_primary) REFERENCES colour(id),
    FOREIGN KEY(colour_secondary) REFERENCES colour(id),
    CHECK (height_min <= height_max),
    CHECK (weight_min <= weight_max)

)''')

    cursor.executemany(f"INSERT INTO {table_name}(species_family, species_type, name, colour_primary, colour_secondary, height_min, height_max, weight_min, weight_max) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", list(list_name))

    cursor.execute(f"DROP VIEW IF EXISTS vw_{table_name}")

    cursor.execute(f'''
    CREATE VIEW vw_{table_name} AS
    SELECT
       tn.id AS id,
       sf.id AS sfid,
       sf.name AS species_family,
       st.id AS stid,
       st.name AS species_type,
       tn.name AS name,
       cp.id AS cpid,
       cp.name AS colour_primary,
       cs.id AS csid,
       cs.name AS colour_secondary,
       tn.height_min AS height_min,
       tn.height_max AS height_max,
       tn.weight_min AS weight_min,
       tn.weight_max AS weight_max
    FROM {table_name} AS tn
    INNER JOIN colour AS cp ON tn.colour_primary = cp.id
    INNER JOIN colour AS cs ON tn.colour_secondary = cs.id
    INNER JOIN species_type AS st ON tn.species_type = st.id
    INNER JOIN species_family AS sf ON tn.species_family = sf.id
''')

    # make changes permanent
    connection.commit()
