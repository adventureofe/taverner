import pandas as pd
import sqlite3
from dataclasses import dataclass
from typing import List, Tuple, Optional


@dataclass
class SQLTable:
    name: str
    columns: List[str]
    foreign_keys: List[str]
    values: List[Tuple]
    view_query: str
    insert_query : str

    def drop(self, connection, cursor):
        cursor.execute(f"DROP TABLE IF EXISTS {self.name}")

    def print(self, connection, cursor):
        # Execute the query to get data from the view
        rows = cursor.execute(f"SELECT * FROM vw_{self.name}").fetchall()

        # Get column names from cursor description
        column_names = [description[0] for description in cursor.description]

        # Print headers
        headers = " | ".join(column_names)  # Print the header row
        print("-" * len(headers))
        print(headers)
        print("-" * len(headers))

        # Print each row in a table format
        for r in rows:
            print(" | ".join(map(str, r)))

        print()

    def change_print(self, connection, cursor):
        print(f"({self.name})(total connection changes)=>{connection.total_changes}")


    def to_df(self, connection, cursor) -> pd.DataFrame:
        query = f"SELECT * FROM vw_{self.name}"
        return pd.read_sql_query(query, connection)

    def create(self, connection, cursor):
        self.drop(connection, cursor)
        self.drop_view(connection, cursor)
        self.init(connection, cursor)
        self.insert(connection, cursor)
        self.create_view(connection, cursor)

    def init(self, connection, cursor):
        foreign_keys_sql = f", {', '.join(self.foreign_keys)}" if self.foreign_keys else ""
        columns_sql = ', '.join(self.columns)
        cursor.execute(f'''
        CREATE TABLE {self.name}
        (
            {columns_sql}
            {foreign_keys_sql}
        )''')

    def insert(self, connection, cursor):
        cursor.executemany(self.insert_query, self.values)

    def create_view(self, connection, cursor):
        self.drop_view(connection, cursor)
        cursor.execute(f'''
        CREATE VIEW vw_{self.name} AS
        {self.view_query}
        ''')

    def drop_view(self, connection, cursor):
        cursor.execute(f"DROP VIEW IF EXISTS vw_{self.name}")


def base_table_create(connection, cursor, table_name, values):
    table = SQLTable(
        name=table_name,

        columns=[
            "id INTEGER PRIMARY KEY AUTOINCREMENT",
            "name TEXT NOT NULL CHECK(length(name) <= 128)"
        ],

        foreign_keys=[],
        values = values,

        view_query=f'''
        SELECT tn.id AS id,
        tn.name AS name
        FROM {table_name} AS tn
        ''',

        insert_query=f"INSERT INTO {table_name} (name) VALUES (?)"
    )

    table.create(connection, cursor)
    table.change_print(connection, cursor)
    return table
