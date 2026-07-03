import sqlite3
from logo import logos
import getpass
from twod_list_maker import list_maker
from  randomgen import randomgenerator
from database_to_dict import database_to_dict
logos()
input_username = input("username: ")


connection1 = sqlite3.connect("users.db")
cursor1 = connection1.cursor()
cursor1.execute("""
CREATE TABLE IF NOT EXISTS users(
            username TEXT PRIMARY KEY,
            password TEXT)
""")
cursor1.execute("SELECT * FROM users ")
users = database_to_dict(cursor1.fetchall())





if input_username in users:
    input_password_1 = getpass.getpass("sudo: ")
    if input_password_1 == users[input_username]:
        connection = sqlite3.connect("encyption_keys.db")
        cursor = connection.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS encryptionkeys(
                    encryption_key TEXT PRIMARY KEY,
                    encryption_value TEXT)
        """)
        cursor.execute("SELECT * FROM encryptionkeys ")
        cheker = cursor.fetchall()
        if len(cheker) == 0 :
            user_request= input("would you like to enter your Decryption key(y/n): ")
            if user_request == "y":
                user_encryption_key = input("key: ")
                cursor.execute("DELETE FROM encryptionkeys ")
                updated_encryption_key = list_maker(user_encryption_key)
                for key in updated_encryption_key:
                    cursor.execute("INSERT INTO encryptionkeys( encryption_key , encryption_value) VALUES(?,?)", (key[0] , key[1]))
                print("Encryption key updated sucessfully...")
                cursor.execute("SELECT * FROM encryptionkeys ")
                encrypt_demo = cursor.fetchall()
                encrypt1 = database_to_dict(encrypt_demo)
                connection.commit()
            elif user_request == "n":
                user_random_generation_agreement = input("Would you like to generate a random Encryption key(y/n): ")
                if user_random_generation_agreement == "y":
                    random_generated_string = randomgenerator()
                    random_generated_list = list_maker(random_generated_string)
                    for key_letter in random_generated_list:
                        cursor.execute("INSERT INTO encryptionkeys(encryption_key, encryption_value) VALUES(?,?)", (key_letter[0], key_letter[1]))
                    print(random_generated_string)
                    cursor.execute("SELECT * FROM encryptionkeys ")
                    encrypt_demo = cursor.fetchall()
                    encrypt1 = database_to_dict(encrypt_demo)
                    connection.commit()
                    print("Encryption key was generated and was added as a key...")
        else:
            cursor.execute("SELECT * FROM encryptionkeys ")
            encrypt_demo = cursor.fetchall()
            encrypt1 = database_to_dict(encrypt_demo)           
            Decrypter  = {value: key for key, value in encrypt1.items()}
        while True:
            user_input = input('> ')
            user_covert_input = list(user_input)
            return_list = []
            if user_input == "exit":
                break
            if user_input.lower() == "config":
                user_request= input("would you like to change your Decryption key/ Regenerate Encryption key(d/r): ")
                if user_request == "d":
                    user_encryption_key = input("key: ")
                    cursor.execute("DELETE FROM encryptionkeys ")
                    updated_encryption_key = list_maker(user_encryption_key)
                    for key in updated_encryption_key:
                        cursor.execute("INSERT INTO encryptionkeys( encryption_key , encryption_value) VALUES(?,?)", (key[0] , key[1]))
                    print("Encryption key updated sucessfully...")
                    cursor.execute("SELECT * FROM encryptionkeys ")
                    encrypt_demo = cursor.fetchall()
                    encrypt1 = database_to_dict(encrypt_demo)
                    Decrypter  = {value: key for key, value in encrypt1.items()}
                    connection.commit()
                elif user_request == "r":
                    user_random_generation_agreement = input("Would you like to generate a random Encryption key(y/n): ")
                    if user_random_generation_agreement == "y":
                        random_generated_string = randomgenerator()
                        random_generated_list = list_maker(random_generated_string)
                        cursor.execute("DELETE FROM encryptionkeys ")                        
                        for key_letter in random_generated_list:
                            cursor.execute("INSERT INTO encryptionkeys(encryption_key, encryption_value) VALUES(?,?)", (key_letter[0], key_letter[1]))
                        print(random_generated_string)
                        cursor.execute("SELECT * FROM encryptionkeys ")
                        encrypt_demo = cursor.fetchall()
                        encrypt1 = database_to_dict(encrypt_demo)
                        Decrypter  = {value: key for key, value in encrypt1.items()}
                        connection.commit()
                        print("Encryption key was generated and was added as a key...")
                elif user_request == "panic":
                    cursor.execute("DELETE FROM encryptionkeys ")
                    print("DataBase is clear")
                    cursor.execute("SELECT * FROM encryptionkeys ")
                    encrypt_demo = cursor.fetchall()
                    encrypt1 = database_to_dict(encrypt_demo)
                    Decrypter  = {value: key for key, value in encrypt1.items()}
                    connection.commit()
                elif user_request == "user":
                    command = input("are you sure you want to delete your user account(y/n): ")
                    if command == "y":
                        cursor1.execute("DELETE FROM users WHERE username = (?)", (input_username,))
                        connection1.commit()
            if len(user_covert_input) !=0 :
                if user_covert_input[-1] == "E" and user_input !="config":
                    cursor1.execute("SELECT * FROM encryptionkeys ")
                    encrypt_demo = cursor1.fetchall()
                    encrypt1 = database_to_dict(encrypt_demo)
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
        cursor1.execute("INSERT INTO users(username, password) VALUES(?,?)", (input_username, new_user_password))
        connection1.commit()
        print("user created successfully...")

    elif new_user == "n":
        user_reponse = input("Do you have an encryption key(y/n): ")
        if user_reponse == "y":
            key = input("Key: ")
            unknown_user_two_d  = list_maker(key)
            encrypt1 = database_to_dict(unknown_user_two_d)        
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
                two_dimentional = list_maker(key)
                dict_1 = database_to_dict(two_dimentional)
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


         
    
          