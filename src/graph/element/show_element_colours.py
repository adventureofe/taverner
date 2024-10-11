import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import math

def visualize_element_colors(db_path):
    # Connect to the SQLite database
    connection = sqlite3.connect(db_path)

    # Query to select all elements with their associated color RGB values
    query = '''
    SELECT
        e.name AS element_name,
        c.r,
        c.g,
        c.b
    FROM element AS e
    INNER JOIN colour AS c ON e.colour = c.id
    '''

    df = pd.read_sql_query(query, connection)

    if df.empty:
        print("No elements found in the 'element' table.")
        return

    # Define number of rows and columns for visualization
    n_elements = len(df)
    n_rows = 3  # Number of rows to display
    n_cols = math.ceil(n_elements / n_rows)  # Calculate columns based on total elements

    # Create the plot
    fig, ax = plt.subplots(figsize=(10, 5))

    # Create a color patch for each element color
    for idx, row in df.iterrows():
        col = idx % n_cols
        row_idx = idx // n_cols

        # Normalize RGB values to [0, 1]
        color = (row['r'] / 255, row['g'] / 255, row['b'] / 255)

        # Create rectangle
        ax.add_patch(plt.Rectangle((col, row_idx), 1, 1, color=color))
        ax.text(col + 0.5, row_idx + 0.5, row['element_name'], ha='center', va='center', fontsize=10, color='white')

    # Set limits and hide axes
    ax.set_xlim(0, n_cols)
    ax.set_ylim(0, n_rows)
    ax.axis('off')

    # Show the plot
    plt.tight_layout()
    plt.show()

    # Close the connection
    connection.close()

if __name__ == "__main__":
    db_path = '../../../taverner.db'  # Replace with your actual database path
    visualize_element_colors(db_path)
