import sqlite3
from collections import defaultdict

def find_adjectives_any_color():
    # Connect to the SQLite database
    connection = sqlite3.connect("../../taverner.db")
    cursor = connection.cursor()

    # Query to find adjectives that are associated with any color
    query = '''
    SELECT DISTINCT a.name
    FROM adjective AS a
    JOIN colour_adjective AS ca ON a.id = ca.adjective
    '''
    
    # Execute the query
    cursor.execute(query)
    
    # Fetch all results
    adjectives = cursor.fetchall()

    # Create a dictionary to group adjectives by their starting letter
    grouped_adjectives = defaultdict(list)
    for adjective in adjectives:
        name = adjective[0]
        starting_letter = name[0].upper()  # Use uppercase for consistency
        grouped_adjectives[starting_letter].append(name)

    # Print the grouped adjectives alphabetically
    print("Adjectives that can be any color, grouped by starting letter:")
    for letter in sorted(grouped_adjectives.keys()):
        print(f"{letter}: {', '.join(sorted(grouped_adjectives[letter]))}")

    # Close the connection
    connection.close()

if __name__ == "__main__":
    find_adjectives_any_color()
