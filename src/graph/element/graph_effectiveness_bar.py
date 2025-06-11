import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

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
        return None

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

    # Sort the results
    sorted_effectiveness_counts = dict(sorted(effectiveness_counts.items()))
    element_totals = []

    for element, counts in sorted_effectiveness_counts.items():
        sorted_effectiveness_counts[element]['Atk'] = {k: sorted_effectiveness_counts[element]['Atk'][k] for k in effectiveness_order if k in sorted_effectiveness_counts[element]['Atk']}
        sorted_effectiveness_counts[element]['Def'] = {k: sorted_effectiveness_counts[element]['Def'][k] for k in effectiveness_order if k in sorted_effectiveness_counts[element]['Def']}

        # Calculate the total cost for each element
        total_cost_atk = sum(len(defenders) * effectiveness_costs[eff_type] for eff_type, defenders in counts['Atk'].items())
        total_cost_def = -sum(len(attackers) * effectiveness_costs[eff_type] for eff_type, attackers in counts['Def'].items())

        element_total = total_cost_atk + total_cost_def
        element_totals.append({'element': element, 'total_cost': element_total})

    return element_totals

def plot_totals(element_totals):
    # Convert to DataFrame for plotting
    df_totals = pd.DataFrame(element_totals)

    # Plotting
    plt.figure(figsize=(12, 8))
    df_totals.plot(kind='bar', x='element', y='total_cost', legend=False)
    plt.title('Total Effectiveness Costs for Each Element')
    plt.xlabel('Element')
    plt.ylabel('Total Cost')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    db_path = '../../../taverner.db'  # Replace with your actual database path
    element_totals = get_effectiveness_counts(db_path)
    if element_totals:
        plot_totals(element_totals)
