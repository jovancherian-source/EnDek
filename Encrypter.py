import sqlite3
from IMGtext_files import logos
import IMGtext_files
import getpass
from Converters import twod_list_maker
from  randomgen import randomgenerator
from Converters import database_to_dict
from Converters import database_to_string
logos()
while True:
    input_username = input("username: ")


    connection1 = sqlite3.connect("users.db")
    cursor1 = connection1.cursor()
    cursor1.execute("""
    CREATE TABLE IF NOT EXISTS users(
                username TEXT PRIMARY KEY,
                password TEXT)
    """)
    cursor1.execute("SELECT * FROM users ")
    users = database_to_dict.database_to_dict(cursor1.fetchall())


    if input_username in users:
        input_password_1 = getpass.getpass("sudo: ")
        if input_password_1 == users[input_username]:
            connection = sqlite3.connect("encyption_keys.db")
            cursor = connection.cursor()
            cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS "{input_username}"(
                        encryption_key TEXT PRIMARY KEY,
                        encryption_value TEXT)
            """)
            connection.commit()
            cursor.execute(f'SELECT * FROM "{input_username}"') 
            cheker = cursor.fetchall()
            if len(cheker) == 0 :
                user_request= input("would you like to enter your Decryption key(y/n): ")
                if user_request == "y":
                    user_encryption_key = input("key: ")
                    cursor.execute(f'DELETE FROM "{input_username}"')
                    updated_encryption_key = twod_list_maker.list_maker(user_encryption_key)
                    for key in updated_encryption_key:
                        cursor.execute(f'INSERT INTO "{input_username}"( encryption_key , encryption_value) VALUES(?,?)', (key[0] , key[1]))
                    print("Encryption key updated sucessfully...")
                    cursor.execute(f'SELECT * FROM "{input_username}"')
                    encrypt_demo = cursor.fetchall()
                    encrypt1 = database_to_dict.database_to_dict(encrypt_demo)
                    connection.commit()
                elif user_request == "n":
                    user_random_generation_agreement = input("Would you like to generate a random Encryption key(y/n): ")
                    if user_random_generation_agreement == "y":
                        random_generated_string = randomgenerator()
                        random_generated_list = twod_list_maker.list_maker(random_generated_string)
                        for key_letter in random_generated_list:
                            cursor.execute(f'INSERT INTO "{input_username}"(encryption_key, encryption_value) VALUES(?,?)', (key_letter[0], key_letter[1]))
                        print(random_generated_string)
                        cursor.execute(f'SELECT * FROM "{input_username}"')
                        encrypt_demo = cursor.fetchall()
                        encrypt1 = database_to_dict.database_to_dict(encrypt_demo)
                        connection.commit()
                        print("Encryption key was generated and was added as a key...")
            else:
                cursor.execute(f'SELECT * FROM "{input_username}"')
                encrypt_demo = cursor.fetchall()
                encrypt1 = database_to_dict.database_to_dict(encrypt_demo)           
                Decrypter  = {value: key for key, value in encrypt1.items()}
            while True:
                user_input = input('> ')
                user_covert_input = list(user_input)
                return_list = []
                if user_input == "exit":
                    break
                if user_input.lower() == "config":
                    user_request= input(IMGtext_files.EnDek_config_logo())
                    if user_request == "1":
                        user_request_1 = IMGtext_files.EnDek_encyption_settings_menu()
                        if user_request_1 == "1":
                            user_encryption_key = input("key: ")
                            if len(user_encryption_key) != 0:
                                cursor.execute(f'DELETE FROM "{input_username}"')
                                updated_encryption_key = twod_list_maker.list_maker(user_encryption_key)
                                for key in updated_encryption_key:
                                    cursor.execute(f'INSERT INTO "{input_username}"( encryption_key , encryption_value) VALUES(?,?)', (key[0] , key[1]))
                                print("Encryption key updated sucessfully...")
                                cursor.execute(f'SELECT * FROM "{input_username}"')
                                encrypt_demo = cursor.fetchall()
                                encrypt1 = database_to_dict.database_to_dict(encrypt_demo)
                                Decrypter  = {value: key for key, value in encrypt1.items()}
                                connection.commit()
                            elif len(user_encryption_key) == 0:
                                print("Encryption key cannot be empty...")
                        elif user_request_1 == "2":
                            user_random_generation_agreement = input("Would you like to generate a random Encryption key(y/n): ")
                            if user_random_generation_agreement == "y":
                                random_generated_string = randomgenerator()
                                random_generated_list = twod_list_maker.list_maker(random_generated_string)
                                cursor.execute(f'DELETE FROM "{input_username}"')
                                for key_letter in random_generated_list:
                                    cursor.execute(f'INSERT INTO "{input_username}"(encryption_key, encryption_value) VALUES(?,?)', (key_letter[0], key_letter[1]))
                                print(random_generated_string)
                                cursor.execute(f'SELECT * FROM "{input_username}"')
                                encrypt_demo = cursor.fetchall()
                                encrypt1 = database_to_dict.database_to_dict(encrypt_demo)
                                Decrypter  = {value: key for key, value in encrypt1.items()}
                                connection.commit()
                                print("Encryption key was generated and was added as a key...")
                        elif user_request_1 == "3":
                            user_database_security = getpass.getpass("sudo: ")
                            if user_database_security == users[input_username]:
                                cursor.execute(f'SELECT * FROM "{input_username}"')
                                encrypt_demo = cursor.fetchall()
                                if len(encrypt_demo) == 0:
                                    print("No encryption key found...")
                                else:
                                    returned_string = database_to_string.database_to_string(encrypt_demo)
                                    print("Encryption key: " + returned_string)
                                    print("Encryption key exported successfully...")
                    elif user_request == "3":
                        user_request_3 = IMGtext_files.Database_settings_menu()
                        if user_request_3 == "1":
                            cursor.execute(f'DELETE FROM "{input_username}"')
                            connection.commit()
                            print("DataBase is clear")
                            cursor.execute(f'SELECT * FROM "{input_username}"') 
                            encrypt_demo = cursor.fetchall()
                            encrypt1 = database_to_dict.database_to_dict(encrypt_demo)
                            Decrypter  = {value: key for key, value in encrypt1.items()}
                    elif user_request == "2":
                        user_request_2 = IMGtext_files.Account_settings_menu()
                        if user_request_2 == "2":
                            conformation = IMGtext_files.Account_confirmation_menu()
                            if conformation == "1":
                                cursor1.execute(f'DELETE FROM users WHERE username = (?)', (input_username,))
                                connection1.commit()
                                cursor.execute(f'DELETE FROM "{input_username}"')
                                connection.commit()
                                print("Account deleted successfully...")
                        elif user_request_2 == "1":
                            break
                if len(user_covert_input) !=0 :
                    if user_covert_input[-1] == "E" and user_input !="config":
                        cursor.execute(f'SELECT * FROM "{input_username}"')
                        encrypt_demo = cursor.fetchall()
                        encrypt = database_to_dict.database_to_dict(encrypt_demo)
                        Decrypter  = {value: key for key, value in encrypt1.items()}
                        for i in user_covert_input:
                            if i in Decrypter:
                                return_list.append(Decrypter.get(i , "letter not found :("))
                        return_word = "". join(return_list)
                        print(return_word)
                    if user_covert_input[-1] != "E" and user_input !="config":
                        for i in user_covert_input :
                            try:
                                return_list.append(encrypt1[i])               
                                if len(user_covert_input) == len(return_list):
                                    return_list.append("E")
                                    return_sentence = "". join(return_list)
                                    print(return_sentence)
                            except KeyError:
                                print("invalid characters")
        elif input_password_1 != users.get(input_username):
            print("wrong password!!")
    elif input_username not in users:
        new_user = input("user not found. would you like to create a new user(y/n): ")
        if new_user == "y":
            new_user_password = getpass.getpass("password: ")
            recheck = getpass.getpass("Re-enter password: ")
            if new_user_password == recheck:
                cursor1.execute("INSERT INTO users(username, password) VALUES(?,?)", (input_username, new_user_password))
                connection1.commit()
                print("user created successfully...")
            else:
                print("passwords do not match!!")

        elif new_user == "n":
            user_reponse = input("Do you have an encryption key(y/n): ")
            if user_reponse == "y":
                key = input("Key: ")
                unknown_user_two_d  = twod_list_maker.list_maker(key)
                encrypt1 = database_to_dict.database_to_dict(unknown_user_two_d)        
                x = 0
                while  x < 5:
                        x += 1
                        user_input = input('> ')
                        user_covert_input = list(user_input)
                        return_list = []
                        if user_input == "exit":
                            break
                        for i in user_covert_input:
                            try:
                                return_list.append(encrypt1[i])               
                                return_sentence = "" . join(return_list)
                                if len(user_covert_input) == len(list(return_sentence)):
                                    return_list.append("E")
                                    return_sentence = "".join(return_list)                         
                                    print(return_sentence)
                            except KeyError:
                                if user_covert_input[-1] == "E":
                                    print("you cannot decrypt without a username")
                                else:
                                    print("invalid characters")
            elif user_reponse == "n":
                user_request= input("would you like to generate Encryption key(y/n): ")
                if user_request == "y":
                    key = randomgenerator()
                    two_dimentional = twod_list_maker.list_maker(key)
                    dict_1 = database_to_dict.database_to_dict(two_dimentional)
                    print(key)
                    print("command successful...")
                    x =0 
                    while x <6:
                        x += 1
                        user_input = input('> ')
                        user_covert_input = list(user_input)
                        return_list = []
                        if user_input == "exit":
                            break
                        for i in user_covert_input:
                            try:
                                return_list.append(dict_1[i])               
                                return_sentence = "" . join(return_list)
                                if len(user_covert_input) == len(list(return_sentence)):
                                    return_list.append("E")
                                    return_sentence = "".join(return_list) 
                                    print(return_sentence)
                            except KeyError:
                                if user_covert_input[-1] == "E":
                                    print("you cannot decrypt without a username")
                                else:
                                    print("invalid characters")    

