import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import math

def plot_colors(database_path):
    # Connect to the SQLite database
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()

    # Query to select all colors from the colour table
    query = "SELECT name, r, g, b FROM colour"

    # Execute the query
    cursor.execute(query)

    # Fetch all results
    results = cursor.fetchall()

    # Get column names from the cursor description
    columns = [column[0] for column in cursor.description]

    # Create a DataFrame from the results
    df = pd.DataFrame(results, columns=columns)

    # Check if the DataFrame is empty
    if df.empty:
        print("No data found in the 'colour' table.")
        return

    # Define number of rows and columns
    n_colors = len(df)
    n_rows = 5  # Number of rows to display
    n_cols = math.ceil(n_colors / n_rows)  # Calculate columns based on total colors

    # Create the plot
    fig, ax = plt.subplots(figsize=(10, 5))

    # Create a color patch for each color
    for idx, color_row in df.iterrows():
        # Calculate row and column index
        col = idx % n_cols
        row = idx // n_cols

        # Ensure the RGB values are normalized to [0, 1]
        color = (color_row['r'] / 255, color_row['g'] / 255, color_row['b'] / 255)

        # Create rectangle
        ax.add_patch(plt.Rectangle((col, row), 1, 1, color=color))

        # Calculate text color for better contrast
        text_color = 'white' if sum(color) < 1.5 else 'black'  # Simple brightness check
        ax.text(col + 0.5, row + 0.5, color_row['name'], ha='center', va='center', fontsize=10, color=text_color)

    # Set limits and hide axes
    ax.set_xlim(0, n_cols)
    ax.set_ylim(0, n_rows)
    ax.axis('off')

    # Show the plot
    plt.tight_layout()  # Optional: adjust the layout to prevent clipping
    plt.show()

    # Close the cursor and connection
    cursor.close()
    connection.close()

if __name__ == "__main__":
    plot_colors('../../../taverner.db')  # Adjust the path to your database file
