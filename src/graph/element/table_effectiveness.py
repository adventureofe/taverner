import sqlite3
import pandas as pd

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
        return

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
    grand_total = 0
    for element in sorted_effectiveness_counts:
        sorted_effectiveness_counts[element]['Atk'] = {k: sorted_effectiveness_counts[element]['Atk'][k] for k in effectiveness_order if k in sorted_effectiveness_counts[element]['Atk']}
        sorted_effectiveness_counts[element]['Def'] = {k: sorted_effectiveness_counts[element]['Def'][k] for k in effectiveness_order if k in sorted_effectiveness_counts[element]['Def']}

    # Format the results
    result = ""
    for element, counts in sorted_effectiveness_counts.items():
        result += f"\n{element} Attacking...\n"
        total_cost_atk = 0
        for eff_type, defenders in counts['Atk'].items():
            if eff_type == "neutral":
                result += f"\t\t{len(defenders)} {eff_type} ({len(defenders) * effectiveness_costs[eff_type]})\n"
            else:
                cost = len(defenders) * effectiveness_costs[eff_type]
                result += f"\t\t{len(defenders)} {eff_type} ({', '.join(sorted(defenders))}) ({cost})\n"
                total_cost_atk += cost
        result += f"\tattack total ({total_cost_atk})\n"

        result += f"{element} Defending...\n"
        total_cost_def = 0
        for eff_type, attackers in counts['Def'].items():
            if eff_type == "neutral":
                result += f"\t\t{len(attackers)} {eff_type} ({len(attackers) * effectiveness_costs[eff_type]})\n"
            else:
                cost = len(attackers) * effectiveness_costs[eff_type]
                result += f"\t\t{len(attackers)} {eff_type} ({', '.join(sorted(attackers))}) ({-cost})\n"
                total_cost_def -= cost
        result += f"\tdefend total ({total_cost_def})\n"

        element_total = total_cost_atk + total_cost_def
        result += f"total ({element_total})\n"

        grand_total += element_total

    return result

if __name__ == "__main__":
    db_path = '../../../taverner.db'  # Replace with your actual database path
    effectiveness_summary = get_effectiveness_counts(db_path)
    print(effectiveness_summary)
