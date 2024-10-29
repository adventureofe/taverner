import sqlite3
import pytest
from src.sql.sql_table import SQLTable, Config
from src.sql.colour.colour import colour_create
from src.sql.element.element import element_create

def test_colour_create(db_connection, colour_darkness, colour_base):
    connection, cursor = db_connection

    values = [
        ("colourless", 255, 255, 255, 1, 1),
        ("black", 0, 0, 0, 2, 2),
        ("white", 255, 255, 255, 3, 2),
        ("light grey", 192, 192, 192, 5, 2),
        ("grey", 128, 128, 128, 4, 2),
        ("dark grey", 64, 64, 64, 6, 2),
        ("light blue", 173, 216, 230, 5, 3),
        ("blue", 0, 0, 255, 4, 3),
        ("navy", 0, 0, 128, 6, 3),
        ("pink", 255, 182, 193, 5, 4),
        ("red", 255, 0, 0, 4, 4),
        ("maroon", 139, 0, 0, 6, 4),
        ("light green", 144, 238, 144, 5, 5),
        ("green", 0, 128, 0, 4, 5),
        ("dark green", 0, 100, 0, 6, 5),
        ("yellow", 255, 255, 0, 4, 6),
        ("dark yellow", 204, 204, 0, 6, 6),
        ("lavender", 230, 230, 250, 5, 7),
        ("purple", 128, 0, 128, 4, 7),
        ("indigo", 75, 0, 130, 6, 7),
        ("peach", 255, 218, 185, 5, 8),
        ("orange", 255, 165, 0, 4, 8),
        ("dark orange", 255, 140, 0, 6, 8),
        ("tan", 210, 180, 140, 5, 9),
        ("brown", 165, 42, 42, 4, 9),
        ("dark brown", 101, 67, 33, 6, 9),
        ("cyan", 0, 255, 255, 4, 3),
        ("lime", 96, 255, 96, 5, 5),
        ("magenta", 255, 0, 255, 4, 7),
        ("silver", 192, 192, 192, 7, 2),
        ("gold", 239, 191, 4, 7, 6),
        ("brass", 181, 166, 66, 7, 9),
        ("platinum", 229, 228, 226, 7, 2)
    ]

    # Call the function to create the colour table and insert values
    table = colour_create(connection, cursor, values=values)

    # Verify that the colour table was created
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='colour';")
    assert cursor.fetchone() is not None

    # Verify the values were inserted correctly
    cursor.execute("SELECT * FROM colour;")
    rows = cursor.fetchall()
    assert len(rows) == len(values)

def test_element_create(db_connection):
    connection, cursor = db_connection

    # Set up the expected values for testing
    values = [
        ("Fire", 1, 1),  # Example values
        ("Water", 2, 1),
        ("Earth", 3, 2),
    ]

    # Create the necessary tables for foreign key references
    cursor.execute(f'''CREATE TABLE colour (
    {Config.id},
    {Config.name},
    r INTEGER,
    g INTEGER,
    b INTEGER,
    darkness INTEGER,
    base INTEGER)''')

    cursor.execute(f'''INSERT INTO colour (name, r, g, b, darkness, base) VALUES
    ('Red', 255, 0, 0, 1, 1),
    ('Green', 0, 255, 0, 2, 1),
    ('Blue', 0, 0, 255, 1, 2)''')

    cursor.execute(f'''CREATE TABLE element_type ({Config.id}, {Config.name})''')
    cursor.execute("INSERT INTO element_type (name) VALUES ('Type1'), ('Type2')")

    # Call the function to create the element table and insert values
    table = element_create(connection, cursor, name="element", values=values)

    # Verify that the element table was created
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='element';")
    assert cursor.fetchone() is not None

    # Verify the values were inserted correctly
    cursor.execute("SELECT * FROM element;")
    rows = cursor.fetchall()
    assert len(rows) == len(values)
