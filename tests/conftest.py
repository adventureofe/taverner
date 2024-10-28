import sqlite3
import pytest
from src.sql.sql_table import SQLTable, Config
from src.sql.colour.colour import colour_create
from src.sql.element.element import element_create

@pytest.fixture
def db_connection():
    # Create an in-memory SQLite database for testing
    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()
    yield connection, cursor
    connection.close()


@pytest.fixture
def colour_darkness(db_connection):
    connection, cursor = db_connection

    # Create the colour_darkness table
    cursor.execute(f'''CREATE TABLE colour_darkness ({Config.id}, {Config.name})''')
    cursor.execute(f'''INSERT INTO colour_darkness (name) VALUES
    ('transparent'),
    ('black'),
    ('white'),
    ('none'),
    ('light'),
    ('dark'),
    ('metallic')''')

    # Commit the changes
    connection.commit()

    # Yield the cursor or any necessary objects for the test
    yield cursor

    # Teardown: drop the table after tests are done
    cursor.execute("DROP TABLE IF EXISTS colour_darkness")
    connection.commit()

@pytest.fixture
def colour_base(db_connection):
    connection, cursor = db_connection

    # Create the colour_darkness table
    cursor.execute(f'''CREATE TABLE colour_base ({Config.id}, {Config.name})''')
    cursor.execute(f'''INSERT INTO colour_base (name) VALUES
    ('none'),
    ('grey'),
    ('blue'),
    ('red'),
    ('green'),
    ('yellow'),
    ('purple'),
    ('orange'),
    ('brown')''')

    # Commit the changes
    connection.commit()

    # Yield the cursor or any necessary objects for the test
    yield cursor

    # Teardown: drop the table after tests are done
    cursor.execute("DROP TABLE IF EXISTS colour_base")
    connection.commit()
