import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def get_strongest_moves(db_path):
    # Connect to the SQLite database
    connection = sqlite3.connect(db_path)

    # Query to select the strongest move for each type along with color information
    query = '''
    SELECT
        m.element,
        m.name,
        MAX(m.pow) AS max_pow,
        c.r,
        c.g,
        c.b
    FROM vw_move m
    JOIN vw_element e ON m.element = e.name
    JOIN vw_colour c ON e.colour = c.name
    GROUP BY m.element
    ORDER BY max_pow DESC
    '''

    df = pd.read_sql_query(query, connection)

    # Close the connection
    connection.close()

    return df

def plot_strongest_moves(df):
    # Convert RGB columns to a format that matplotlib can use
    df['color'] = df.apply(lambda row: (row['r']/255, row['g']/255, row['b']/255), axis=1)

    # Plotting
    plt.figure(figsize=(12, 8))
    bars = plt.bar(df['element'], df['max_pow'], color=df['color'], edgecolor='black')

    # Add move names vertically on the bars
    for bar, move_name in zip(bars, df['name']):
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() / 2,
            move_name,
            ha='center',
            va='center',
            rotation='vertical',
            color='white',
            bbox=dict(facecolor='black', edgecolor='black', boxstyle='round,pad=0.5')
        )

    plt.title('Strongest Move for Each Element')
    plt.xlabel('Element')
    plt.ylabel('Power')
    plt.xticks(rotation=45, ha='right')
    plt.yticks(range(0, int(df['max_pow'].max()) + 10, 10))  # Show ticks on the y-axis every 10 units
    plt.grid(axis='y', which='both', linestyle='--', linewidth=0.5)  # Add grid lines
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    db_path = '../../../taverner.db'  # Replace with your actual database path
    df_strongest_moves = get_strongest_moves(db_path)
    plot_strongest_moves(df_strongest_moves)
