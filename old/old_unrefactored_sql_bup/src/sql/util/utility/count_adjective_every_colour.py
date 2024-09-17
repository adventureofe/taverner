import sqlite3
from collections import defaultdict

def count_adjectives_any_color():
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

    # Create a dictionary to count adjectives by their starting letter
    letter_counts = defaultdict(int)
    for adjective in adjectives:
        name = adjective[0]
        starting_letter = name[0].upper()  # Use uppercase for consistency
        letter_counts[starting_letter] += 1

    # Print the counts of adjectives grouped by their starting letter
    print("Count of adjectives that can be any color, grouped by starting letter:")
    for letter in sorted(letter_counts.keys()):
        print(f"{letter}: {letter_counts[letter]}")

    # Close the connection
    connection.close()

if __name__ == "__main__":
    count_adjectives_any_color()
