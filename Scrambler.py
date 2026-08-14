import random
import sqlite3
def pre_scrambler(Encryption_key, username):
        connection = sqlite3.connect("scrambler.db")
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM '{username}'")
        scrambler_key = cursor.fetchall()
        return_index_numbers = []
        for item in scrambler_key:
            return_index_numbers.append(item[1])
        return_encryption_key = []
        for item in scrambler_key:
            return_encryption_key.append(Encryption_key[item[1]])
        return_encryption_key.append('S')
        return ["".join(return_encryption_key), return_index_numbers]
def scrambler(Encryption_key, username):
        connection = sqlite3.connect("scrambler.db")
        cursor = connection.cursor()
        cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS "{username}"(
                    position INTEGER PRIMARY KEY,       
                    index_number INTEGER)
        """)
        cursor.execute(f"DELETE FROM '{username}'")
        index_numbers = list(range(len(Encryption_key)))
        secure_random = random.SystemRandom()
        secure_random.shuffle(index_numbers)
        list_encryption_key = list(Encryption_key)
        return_encryption_key = []
        for index in index_numbers:
            return_encryption_key.append(list_encryption_key[index])
        for index in range(len(index_numbers)):
            cursor.execute(f"INSERT INTO '{username}'(position, index_number) VALUES(?, ?)", (index, index_numbers[index]))
        connection.commit()
        return_encryption_key.append('S')
        return ["".join(return_encryption_key) , index_numbers]
def new_encryption_key_unscrambler(scrambeled_encryption_key, unscrambler , username):
    connection = sqlite3.connect("scrambler.db")
    cursor = connection.cursor()
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS "{username}"(
                    position INTEGER PRIMARY KEY,       
                    index_number INTEGER)
        """)
    cursor.execute(f"DELETE FROM '{username}'")
    index_numbers = unscrambler.strip('[]').split(', ')
    for index in range(len(index_numbers)):
        cursor.execute(f"INSERT INTO '{username}'(position, index_number) VALUES(?, ?)", (index, index_numbers[index]))
    connection.commit()
    usable_index_numbers = []
    for index in range(len(index_numbers)):
        usable_index_numbers.append((index, int(index_numbers[index])))
    return_encryption_key = []
    sorted_index_numbers = sorted(usable_index_numbers, key=lambda x: x[1])
    for item in sorted_index_numbers:
         return_encryption_key.append(scrambeled_encryption_key[item[0]])
    return "".join(return_encryption_key)
def user_panic(username):
    connection = sqlite3.connect("scrambler.db")
    cursor = connection.cursor()
    cursor.execute(f"DELETE FROM '{username}'")
    connection.commit()
def unscrambler(scrambled_encryption_key, username):
    connection = sqlite3.connect("scrambler.db")
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM '{username}'")
    index_numbers = cursor.fetchall()
    return_encryption_key = []
    sorted_index_numbers = sorted(index_numbers, key=lambda x: x[1])
    for item in sorted_index_numbers:
         return_encryption_key.append(scrambled_encryption_key[item[0]])
    return "".join(return_encryption_key)