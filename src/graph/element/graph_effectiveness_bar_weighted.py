import matplotlib.pyplot as plt
import sqlite3
import pandas as pd

def get_effectiveness_counts_attacking_only(db_path):
    # Connect to the SQLite database
    connection = sqlite3.connect(db_path)

    # Query to select all element effectiveness data
    query = '''
    SELECT
        attacker,
        defender,
        effectiveness
    FROM vw_element_effectiveness
    '''

    df = pd.read_sql_query(query, connection)

    # Close the connection
    connection.close()

    if df.empty:
        print("No elements found in the 'element_effectiveness' table.")
        return None, None

    # Create a dictionary to store the counts
    effectiveness_counts = {}
    for _, row in df.iterrows():
        attacker = row['attacker']
        effectiveness = row['effectiveness']

        if attacker not in effectiveness_counts:
            effectiveness_counts[attacker] = {}

        if effectiveness not in effectiveness_counts[attacker]:
            effectiveness_counts[attacker][effectiveness] = 0
        effectiveness_counts[attacker][effectiveness] += 1

    # Define the desired order of effectiveness types including "neutral"
    effectiveness_order = ["extra strong", "strong", "somewhat strong", "neutral", "somewhat weak", "weak", "extra weak", "none"]

    # Define the cost for each effectiveness type
    effectiveness_costs = {
        "extra strong": 3,
        "strong": 2,
        "somewhat strong": 1,
        "neutral": 0,
        "somewhat weak": -1,
        "weak": -2,
        "extra weak": -3,
        "none": 0
    }

    # Prepare totals for each element
    element_totals = {element: {eff: 0 for eff in effectiveness_order} for element in effectiveness_counts}

    for element, eff_counts in effectiveness_counts.items():
        for eff_type, count in eff_counts.items():
            element_totals[element][eff_type] = count * effectiveness_costs[eff_type]

    return element_totals, effectiveness_order


def create_stacked_bar_graph_attacking_only(element_totals, effectiveness_order):
    # Prepare data for the graph
    categories = list(element_totals.keys())
    bar_segments = {eff_type: [] for eff_type in effectiveness_order}

    for element in categories:
        for eff_type in effectiveness_order:
            bar_segments[eff_type].append(element_totals[element][eff_type])

    # Create the stacked bar chart
    bottom = [0] * len(categories)
    colors = {
        "extra strong": "darkred",
        "strong": "red",
        "somewhat strong": "orange",
        "neutral": "gray",
        "somewhat weak": "lightblue",
        "weak": "blue",
        "extra weak": "darkblue",
        "none": "white"
    }

    plt.figure(figsize=(10, 6))
    for eff_type in effectiveness_order:
        plt.bar(categories, bar_segments[eff_type], bottom=bottom, label=eff_type, color=colors[eff_type])
        bottom = [b + s for b, s in zip(bottom, bar_segments[eff_type])]

    plt.xlabel("Elements")
    plt.ylabel("Weighted Totals (Attacking Only)")
    plt.title("Weighted Effectiveness Stacked Bar Graph (Attacking Only)")
    plt.legend(title="Effectiveness")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    db_path = '../../../taverner.db'  # Replace with your actual database path

    # Get effectiveness data and totals for attacking only
    element_totals, effectiveness_order = get_effectiveness_counts_attacking_only(db_path)

    if element_totals:
        # Create the stacked bar graph for attacking data only
        create_stacked_bar_graph_attacking_only(element_totals, effectiveness_order)
