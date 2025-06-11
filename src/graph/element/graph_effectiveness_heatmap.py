import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def visualize_element_effectiveness(db_path):
    # Connect to the SQLite database
    connection = sqlite3.connect(db_path)

    # Query to select all element effectiveness data
    query = '''
    SELECT
        ef.attacker AS attacker,
        ef.defender AS defender,
        ef.eid AS effectiveness
    FROM vw_element_effectiveness AS ef
    '''

    df = pd.read_sql_query(query, connection)

    if df.empty:
        print("No elements found in the 'element_effectiveness' table.")
        return

    # Pivot the data for heatmap plotting
    effectiveness_matrix = df.pivot(index="attacker", columns="defender", values="effectiveness")

    # Create the heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(effectiveness_matrix, annot=True, cmap='coolwarm', cbar_kws={'label': 'Effectiveness'})
    plt.title('Element Effectiveness')
    plt.show()

    # Close the connection
    connection.close()

if __name__ == "__main__":
    db_path = '../../../taverner.db'  # Replace with your actual database path
    visualize_element_effectiveness(db_path)
