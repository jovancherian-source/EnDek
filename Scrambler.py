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
        connection.commit()
        connection.close()
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
        connection.close()
        return ["".join(return_encryption_key) , index_numbers]
def new_encryption_key_unscrambler(scrambeled_encryption_key, unscrambler , username):
    special_encryption_key = list(scrambeled_encryption_key.strip('S'))
    scrambler_encryptio_key_usable = []
    for item in special_encryption_key:
        if item != ' ':
            scrambler_encryptio_key_usable.append(item)
    connection = sqlite3.connect("scrambler.db")
    cursor = connection.cursor()
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS "{username}"(
                    position INTEGER PRIMARY KEY,       
                    index_number INTEGER)
        """)
    cursor.execute(f"DELETE FROM '{username}'")
    index_numbers_unpure = list(unscrambler)
    index_numbers_usable =[]
    for item in index_numbers_unpure:
        if item != ' ' and item != "[" and item != "]" and item != ' ':
            index_numbers_usable.append(item)
    index_numbers = "".join(index_numbers_usable).split(",")
    for index in range(len(index_numbers)):
        cursor.execute(f"INSERT INTO '{username}'(position, index_number) VALUES(?, ?)", (index, index_numbers[index]))
    connection.commit()
    usable_index_numbers = []
    for index in range(len(index_numbers)):
        usable_index_numbers.append((index, int(index_numbers[index])))
    return_encryption_key = []
    sorted_index_numbers = sorted(usable_index_numbers, key=lambda x: x[1])
    for item in sorted_index_numbers:
         return_encryption_key.append(scrambler_encryptio_key_usable[item[0]])
    connection.commit()
    connection.close()
    return "".join(return_encryption_key)
def user_panic(username):
    connection = sqlite3.connect("scrambler.db")
    cursor = connection.cursor()
    cursor.execute(f"DELETE FROM '{username}'")
    connection.commit()
    connection.close()
def unscrambler(scrambled_encryption_key, username):
    connection = sqlite3.connect("scrambler.db")
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM '{username}'")
    index_numbers = cursor.fetchall()
    return_encryption_key = []
    sorted_index_numbers = sorted(index_numbers, key=lambda x: x[1])
    for item in sorted_index_numbers:
         return_encryption_key.append(scrambled_encryption_key[item[0]])
    connection.commit()
    connection.close()
    return "".join(return_encryption_key)
def scrambeler_updater(scrambler_key, username):
    connection = sqlite3.connect("scrambler.db")
    cursor = connection.cursor()
    cursor.execute(f"DELETE FROM '{username}'")
    index_numbers = scrambler_key.strip('[]').split(', ')
    for index in range(len(index_numbers)):
        cursor.execute(f"INSERT INTO '{username}'(position, index_number) VALUES(?, ?)", (index, index_numbers[index]))
    connection.commit()
    connection.close()