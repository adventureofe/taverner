def generate_function(connection, cursor, func_list):
    """Creates tables using the provided list of creation functions."""
    for create_func, table_name in func_list:
        try:
            create_func(connection, cursor)
        except Exception as e:
            print(f"ERROR: generate_all {table_name}: {e}")
            continue  # Proceed to the next table
