import sys
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def fetch_colors_from_db(connection):
    """
    Fetch color data from the database.
    """
    query = """
    SELECT name, r, g, b, description
    FROM colors
    """  # Adjust the table name and columns as needed
    return pd.read_sql_query(query, connection)

def plot_colors(color_df):
    """
    Plot colors from the DataFrame using Matplotlib.
    """
    # Set up the plot
    fig, ax = plt.subplots(figsize=(12, 14))
    ax.axis('off')

    # Number of colors
    n = len(color_df)

    # Create a grid of colors
    for i, row in color_df.iterrows():
        color = np.array([row['r'], row['g'], row['b']]) / 255.0  # Normalize RGB values to [0, 1] range
        rect = plt.Rectangle((0, i), 1, 1, color=color, edgecolor='none')
        ax.add_patch(rect)
        ax.text(1.1, i + 0.5, f'{row["name"]}\nRGB: ({row["r"]}, {row["g"]}, {row["b"]})\nDesc: {row["description"]}', 
                va='center', ha='left', fontsize=10)

    # Adjust layout and show plot
    plt.xlim(0, 2)
    plt.ylim(0, n)
    plt.gca().invert_yaxis()  # Reverse the y-axis to have the first color at the top
    plt.show()

def main() -> int:
    # Make connection to sqlite3
    connection = sqlite3.connect("../../../taverner.db")

    # Fetch color data from the database
    color_df = fetch_colors_from_db(connection)

    # Plot the colors
    plot_colors(color_df)

    return 0

if __name__ == "__main__":
    sys.exit(main())
