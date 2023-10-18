import sys
import sqlite3
import pandas as pd


from sql.generate.colour.colour import colour_create




sql_table_drop = lambda cursor, table_name: cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
sql_table_print = lambda cursor, table_name: print(cursor.execute(f"SELECT * FROM {table_name}").fetchall())

sql_change_print = lambda connection : print(f"(total connection changes)=>{connection.total_changes}", end='\n')


def colour_add(name, r, g, b, colour_list):
    return 0

def main() -> int:
    #prompt at program start
    # make connection to sqlite3
    connection = sqlite3.connect("test_data.db")

    #print the number of database rows that have been changed by connection
    # (for testing. no changes have been made yet so should be 0)
    sql_change_print(connection)

    # make a pointer to issue sql statements to database
    cursor = connection.cursor()

    cursor.execute("DROP TABLE IF EXISTS scrabble")
    cursor.execute("CREATE TABLE scrabble (id INTEGER PRIMARY KEY, letter TEXT NOT NULL, english_value INTEGER NOT NULL, english_quantity INTEGER NOT NULL, afrikaans_value INTEGER NOT NULL, afrikaans_quantity INTEGER NOT NULL, german_value INTEGER NOT NULL, german_quantity INTEGER NOT NULL, latin_value INTEGER NOT NULL, latin_quantity INTEGER NOT NULL, irish_value INTEGER NOT NULL, irish_quantity INTEGER NOT NULL, polish_value INTEGER NOT NULL, polish_quantity INTEGER NOT NULL, portuguese_value INTEGER NOT NULL, portuguese_quantity INTEGER NOT NULL, is_vowel BOOLEAN NOT NULL, double_start BOOLEAN NOT NULL, double_mid BOOLEAN NOT NULL, double_end BOOLEAN NOT NULL)")


    # letter, value, quantity, afrikaans_value, afrikaans_quantity, germen_value, german_quanity, latin_value, latin_quantity,  irish_value, irish_quantity, is_vowel, polish_value, polish_quantity, portuguese_value, portuguese_quantity  double_start,double_mid, double_end
    scrabble_list = [('a', 1,  9,  1,  9,  1,  5,  1, 9   ,1   , 13  , 1  , 9  , 1  ,14   , True, False, False, True,),
                     ('e', 1, 12,  1, 16,  1, 15,  1, 11  ,1   , 6  , 1  , 7  , 1  ,11   , True, True, True, True),
                     ('i', 1,  9,  1,  8,  1,  6,  1, 11  ,1   , 10  , 1  ,8   , 1  , 10  , True, False, False, True),
                     ('o', 1,  8,  1,  6,  2,  3,  2, 5  , 2  ,  4 ,  1 ,  6 ,  1 ,10   , True, True, True, True),
                     ('u', 1,  4,  4,  2,  1,  6,   1,7   ,2   , 3  , 0  , 0  ,  1 , 7  , True, False, False, True),
                     ('l', 1,  4,  2,  3,  2,  3,  4 , 2  ,2   ,  4 , 2  , 3  ,  2 , 5  , False, True, True, True),
                     ('n', 1,  6,  1,  8,  1,  9,  1 , 6  ,1   ,  7 , 1  , 5  ,  3 , 4  , False, False, True, True), 
                     ('s', 1,  4,  1,  6,  1,  7,  1 , 8  ,1   ,  6 , 1  , 4  ,  1 , 8  , False, False, True, True),
                     ('t', 1,  6,  1,  6,  1,  6,  1 , 7  ,2   ,  4 , 2  ,  3 ,  1 , 5  , False, False, True, True),
                     ('r', 1,  6,  1,  6,  1,  6,  1 , 9  ,1   ,  7 , 1  ,  4 ,  1 , 6  , False, False, True, True),
                     ('d', 2,  4,  1,  6,  1,  4,  0 , 0  ,2   ,  4 , 2  ,  3 ,  2 , 5  , False, False, True, True),
                     ('g', 2,  3,  2,  4,  2,  3,  6 , 1  ,2   ,  3 , 3  , 2  ,  4 , 2  , False, False, True, True),
                     ('b', 3,  2,  8,  1,  3,  2,  5 , 2  ,10   , 1  , 3  ,  2 , 3  ,3   , False, False, True, True),
                     ('c', 3,  2,  0,  0,  4,  3,  2 , 4  , 2  , 4  , 2  ,  3 ,  2 , 4  , False, False, True, False),
                     ('m', 3,  2,  4,  2,  3,  4,  2 , 5  , 4  , 2  , 2  ,  3 ,  1, 6  , False, False, True, False),
                     ('p', 3,  2,  5,  2,  4,  1,  4 , 2  , 10  , 1  , 2  , 3  ,  2 , 4  , False, False, True, True),
                     ('f', 4,  2,  8,  1,  4,  2,  6 , 1  , 4  , 2  , 5  ,  1 ,  4 , 2  , False, False, True, True),
                     ('h', 4,  2,  2,  3,  2,  4,  10 , 1  ,1   , 10  , 3  , 2  , 4  ,2   , False, False, False, False),
                     ('v', 4,  2,  5,  2,  6,  1,  5 , 2  , 0  ,  0 ,  0 ,  0 , 4  , 2  , False, False, True, False),
                     ('w', 4,  2,  3,  3,  3,  1,  0 , 0  , 0  ,  0 , 1  , 4  ,  0 , 0  , False, False, True, False), 
                     ('y', 4,  2,  4,  2, 10,  1,  0 , 0  , 0  ,  0 , 2  , 4  ,  0 , 0  , True, False, False, False),
                     ('k', 5,  1,  3,  3,  4,  2,  0 , 0  ,  0 ,  0 , 2  , 3  , 0  ,0   , False, False, True, False), 
                     ('j', 8,  1, 10,  1,  6,  1,  0 , 0  ,  0 ,  0 , 3  ,  2 , 5  , 2  , False, False, True, False),
                     ('x', 8,  1,  0,  0,  8,  1,  6 , 1  ,   0,  0 , 0  ,  0 ,  8 , 1  , False, False, False, False), 
                     ('q', 10, 1,  0,  0, 10,  1,  10 , 1  ,  0 , 0  , 0  , 0  , 6  ,1   , False, False, False, False),
                     ('z', 10, 1,  0,  0,  3,  1,  0 , 0  ,  0 , 0  ,  1 , 5  , 8  , 1  , False, False, False, False)]

    cursor.executemany("INSERT INTO scrabble(letter, english_value, english_quantity, afrikaans_value, afrikaans_quantity, german_value, german_quantity, latin_value, latin_quantity, irish_value, irish_quantity, polish_value, polish_quantity, portuguese_value, portuguese_quantity,  is_vowel, double_start, double_mid, double_end) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", scrabble_list)

    # make changes permanent
    connection.commit()

    # get PANDAS dataframe
    colour_create(connection, cursor)
    df_colour = pd.read_sql_query("SELECT * FROM colour", connection)

    df = pd.read_sql_query('SELECT * FROM scrabble', connection)
    print(df_colour)

   #df_scrabble.insert(loc=4, column="can_double", value=[False, True, False, True, False, False, True, True, True, False, True, True, False, True, True, True, True, False, True, False, False, True, False, False, False, False])


    filtered_df = df[(df["irish_quantity"] != 0) & (df["portuguese_quantity"]  != 0)][['letter', 'english_value', 'english_quantity', 'irish_value', 'irish_quantity']]
    print(filtered_df)

    sql_change_print(connection)
    cursor.close()
    connection.close()

    # roll_dice(1, 20, 3)
    return 0

if __name__ == "__main__":
    sys.exit(main())
