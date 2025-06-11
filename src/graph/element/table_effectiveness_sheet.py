import sqlite3
import pandas as pd
from tabulate import tabulate  # Ensure tabulate is installed with pip install tabulate

def get_effectiveness_counts(db_path):
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
        return {}, {}

    # Create a dictionary to store the counts
    effectiveness_counts = {}
    for _, row in df.iterrows():
        attacker = row['attacker']
        defender = row['defender']
        effectiveness = row['effectiveness']

        if attacker not in effectiveness_counts:
            effectiveness_counts[attacker] = {'Atk': {}, 'Def': {}}
        if defender not in effectiveness_counts:
            effectiveness_counts[defender] = {'Atk': {}, 'Def': {}}

        if effectiveness not in effectiveness_counts[attacker]['Atk']:
            effectiveness_counts[attacker]['Atk'][effectiveness] = []
        effectiveness_counts[attacker]['Atk'][effectiveness].append(defender)

        if effectiveness not in effectiveness_counts[defender]['Def']:
            effectiveness_counts[defender]['Def'][effectiveness] = []
        effectiveness_counts[defender]['Def'][effectiveness].append(attacker)

    # Define the desired order of effectiveness types including "neutral"
    effectiveness_order = ["extra strong", "strong", "somewhat strong", "neutral", "somewhat weak", "weak", "extra weak"]

    # Define the cost for each effectiveness type
    effectiveness_costs = {
        "extra strong": 3,
        "strong": 2,
        "somewhat strong": 1,
        "neutral": 0,
        "somewhat weak": -1,
        "weak": -2,
        "extra weak": -3
    }

    # Sort the results
    sorted_effectiveness_counts = dict(sorted(effectiveness_counts.items()))
    for element in sorted_effectiveness_counts:
        sorted_effectiveness_counts[element]['Atk'] = {k: sorted_effectiveness_counts[element]['Atk'][k] for k in effectiveness_order if k in sorted_effectiveness_counts[element]['Atk']}
        sorted_effectiveness_counts[element]['Def'] = {k: sorted_effectiveness_counts[element]['Def'][k] for k in effectiveness_order if k in sorted_effectiveness_counts[element]['Def']}

    return sorted_effectiveness_counts, effectiveness_costs

def display_effectiveness_table(sorted_effectiveness_counts, effectiveness_costs):
    # Create an empty list to hold table rows
    table_rows = []

    for element, counts in sorted_effectiveness_counts.items():
        total_cost_atk = 0
        for eff_type, defenders in counts['Atk'].items():
            count = len(defenders)
            cost = count * effectiveness_costs[eff_type]
            total_cost_atk += cost
            table_rows.append([element, "Attacking", eff_type, count, cost])

        total_cost_def = 0
        for eff_type, attackers in counts['Def'].items():
            count = len(attackers)
            cost = -count * effectiveness_costs[eff_type]
            total_cost_def += cost
            table_rows.append([element, "Defending", eff_type, count, cost])

        element_total = total_cost_atk + total_cost_def
        table_rows.append([element, "Total", "Overall", None, element_total])

    # Convert to DataFrame
    df = pd.DataFrame(table_rows, columns=["Element", "Mode", "Effectiveness", "Count", "Cost"])

    return df

if __name__ == "__main__":
    db_path = '../../../taverner.db'  # Replace with your actual database path

    # Get effectiveness data and costs
    sorted_effectiveness_counts, effectiveness_costs = get_effectiveness_counts(db_path)

    # Generate the effectiveness table
    effectiveness_table = display_effectiveness_table(sorted_effectiveness_counts, effectiveness_costs)

    # Display the table using tabulate
    print(tabulate(effectiveness_table, headers="keys", tablefmt="grid"))
