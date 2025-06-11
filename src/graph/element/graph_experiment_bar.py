mpor matplotlib.pyplot as plt
import sqlite3
import pandas as pd

def calculate_metrics(db_path):
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
        return None

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

    # Initialize results dictionary
    element_metrics = {}

    for _, row in df.iterrows():
        attacker = row["attacker"]
        defender = row["defender"]
        effectiveness = row["effectiveness"]

        if attacker not in element_metrics:
            element_metrics[attacker] = [0, 0, 0, 0, 0, 0]  # Initialize metrics for attacking
        if defender not in element_metrics:
            element_metrics[defender] = [0, 0, 0, 0, 0, 0]  # Initialize metrics for defending

        # Attacking Metrics
        if effectiveness in ["somewhat strong", "strong", "extra strong"]:
            element_metrics[attacker][0] += effectiveness_costs[effectiveness]
        elif effectiveness == "neutral":
            element_metrics[attacker][1] += 1
        elif effectiveness in ["somewhat weak", "weak", "extra weak"]:
            element_metrics[attacker][2] += abs(effectiveness_costs[effectiveness])

        # Defending Metrics
        if effectiveness in ["somewhat strong", "strong", "extra strong"]:
            element_metrics[defender][3] += effectiveness_costs[effectiveness]
        elif effectiveness == "neutral":
            element_metrics[defender][4] += 1
        elif effectiveness in ["somewhat weak", "weak", "extra weak"]:
            element_metrics[defender][5] += abs(effectiveness_costs[effectiveness])

    return element_metrics

def create_grouped_bar_chart(element_metrics):
    # Prepare data for plotting
    elements = list(element_metrics.keys())
    metrics = list(zip(*element_metrics.values()))  # Transpose metrics to group by type
    bar_labels = ["Strong Atk", "Neutral Atk", "Weak Atk", "Strong Def", "Neutral Def", "Weak Def"]
    colors = ["darkred", "gray", "blue", "orange", "lightgray", "lightblue"]

    x = range(len(elements))  # X-axis positions for elements
    bar_width = 0.1  # Width of each bar

    plt.figure(figsize=(12, 6))

    # Create bars for each metric
    for i, (metric, label, color) in enumerate(zip(metrics, bar_labels, colors)):
        positions = [p + i * bar_width for p in x]  # Adjust positions for grouped bars
        plt.bar(positions, metric, width=bar_width, label=label, color=color)

    # Finalize the plot
    plt.xlabel("Elements")
    plt.ylabel("Values")
    plt.title("Effectiveness Metrics by Element")
    plt.xticks([p + bar_width * 2.5 for p in x], elements, rotation=45)  # Center group labels
    plt.legend(title="Metric Types")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    db_path = '../../../taverner.db'  # Replace with your actual database path

    # Calculate metrics
    element_metrics = calculate_metrics(db_path)

    if element_metrics:
        # Create the grouped bar chart
        create_grouped_bar_chart(element_metrics)
