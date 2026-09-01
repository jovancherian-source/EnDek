import sqlite3
import CLI
import getpass
from Converters import twod_list_maker
from  randomgen import randomgenerator
from Converters import database_to_dict
from Converters import database_to_string
from Converters import letter_remover
from Scrambler import scrambler
from Scrambler import new_encryption_key_unscrambler
from Scrambler import user_panic
from Scrambler import pre_scrambler
from Scrambler import scrambeler_updater
from argon2 import PasswordHasher
import string
from Functionalities import updater
CLI.logos()

EnDek_verison = "2.7.0"
EnDek_name = "Ludicrous"
latest_version = updater.intial_update_checker(EnDek_verison)
if latest_version is not None:
    print(latest_version)
class AccoutDeletion(Exception):
    pass
def password_hashing(password):
    ph = PasswordHasher()
    return ph.hash(str(password))
def password_verification(password, hashed_password):
    ph = PasswordHasher()
    try:
        ph.verify(hashed_password, str(password))
        return True
    except Exception:
        return False
def main():
    while True:
        # user authentication and user database connection
        try:
            input_username = input("username: ")
        except KeyboardInterrupt:
            print("Thank You for using EnDek")
            return
        if input_username == "/exit":
            return
        if not all(char in string.ascii_letters for char in input_username):
            print("please only plain English letters are accepted for usernames! Spaces are NOT allowed.")
            main()
        user_db_connection = sqlite3.connect("users.db")
        user_db_cursor = user_db_connection.cursor()
        user_db_cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
                    username TEXT PRIMARY KEY,
                    password TEXT,
                    scrambler BOOLEAN)
        """)
        user_db_cursor.execute("SELECT * FROM users ")
        users = database_to_dict.database_to_dict(user_db_cursor.fetchall())


        if input_username in users:
            # password manager, authentication and database connection.
            try:
                input_password_1 = getpass.getpass("sudo: ")
                if password_verification(input_password_1, users[input_username]):
                    input_password_1 = ""
                    encryption_key_db_connection = sqlite3.connect("encyption_keys.db")
                    encryption_key_cursor = encryption_key_db_connection.cursor()
                    encryption_key_cursor.execute(f"""
                    CREATE TABLE IF NOT EXISTS "{input_username}"(
                                encryption_key TEXT PRIMARY KEY,
                                encryption_value TEXT)
                    """)
                    encryption_key_db_connection.commit()
                    encryption_key_cursor.execute(f'SELECT * FROM "{input_username}"') 
                    cheker = encryption_key_cursor.fetchall()
                elif password_verification(input_password_1, users[input_username]) == False:
                    print("wrong password!!")
                try:
                    trial_times = 0
                    accept_checker = False
                    while len(cheker) == 0 and trial_times < 5 and accept_checker != True:
                        # first time user encryption key setting
                        trial_times += 1
                        user_request= input("would you like to enter your Decryption key(y/n): ")
                        if user_request == "y":
                            user_encryption_key = input("key: ")
                            # userm log-in encryption key with scrambler key
                            def login_user_scrambler_key(user_encryption_key):
                                user_db_cursor.execute("UPDATE users SET scrambler = ? WHERE username = ? " , (True, input_username))
                                user_db_connection.commit()
                                unscrambler_key = input("Scrambler Key: ")
                                user_encryption_key_unscrambled = new_encryption_key_unscrambler(scrambeled_encryption_key = user_encryption_key, unscrambler = unscrambler_key , username = input_username)
                                user_encryption_key_unscrambled = letter_remover.LetterFunctions.letter_adder(user_encryption_key_unscrambled)
                                encryption_key_cursor.execute(f'DELETE FROM "{input_username}"')
                                updated_encryption_key = twod_list_maker.list_maker(user_encryption_key_unscrambled)
                                for key in updated_encryption_key:
                                    encryption_key_cursor.execute(f'INSERT INTO "{input_username}"( encryption_key , encryption_value) VALUES(?,?)', (key[0] , key[1]))
                                print("Encryption key added sucessfully...")
                                encryption_key_cursor.execute(f'SELECT * FROM "{input_username}"')
                                encrypt_demo = encryption_key_cursor.fetchall()
                                encrypt1 = database_to_dict.database_to_dict(encrypt_demo)
                                encryption_key_db_connection.commit()
                                return encrypt1
                            # user log-in encryption key without scrambler key
                            def login_user_encyption_key(user_encryption_key):
                                user_db_cursor.execute("UPDATE users SET scrambler = ? WHERE username = ? " , (False, input_username))
                                user_db_connection.commit()
                                user_encryption_key = letter_remover.LetterFunctions.letter_adder(user_encryption_key)
                                encryption_key_cursor.execute(f'DELETE FROM "{input_username}"')
                                updated_encryption_key = twod_list_maker.list_maker(user_encryption_key)
                                for key in updated_encryption_key:
                                    encryption_key_cursor.execute(f'INSERT INTO "{input_username}"( encryption_key , encryption_value) VALUES(?,?)', (key[0] , key[1]))
                                print("Encryption key added sucessfully...")
                                encryption_key_cursor.execute(f'SELECT * FROM "{input_username}"')
                                encrypt_demo = encryption_key_cursor.fetchall()
                                encrypt1 = database_to_dict.database_to_dict(encrypt_demo)
                                encryption_key_db_connection.commit()
                                user_db_connection.commit()
                                return encrypt1
                            # cheker pipe line for user enryption key 
                            if user_encryption_key == "":
                                print("Encryption key cannot be empty...")
                                accept_checker = False
                            elif user_encryption_key != "":
                                if user_encryption_key[-1] == "S":
                                    accept_checker = True
                                    encrypt1 = login_user_scrambler_key(user_encryption_key)
                                elif user_encryption_key[-1] != "S":   
                                    accept_checker = True 
                                    encrypt1 = login_user_encyption_key(user_encryption_key)
                        # auto generating encryption key for first time log-in
                        def login_random_key_generation():
                            user_db_cursor.execute("UPDATE users SET scrambler = ? WHERE username = ? " , (False, input_username))
                            user_db_connection.commit()
                            user_random_generation_agreement = input("Would you like to generate a random Encryption key(y/n): ")
                            if user_random_generation_agreement == "y":
                                accept_checker = True
                                random_generated_string = randomgenerator()
                                random_generated_list = twod_list_maker.list_maker(random_generated_string)
                                for key_letter in random_generated_list:
                                    encryption_key_cursor.execute(f'INSERT INTO "{input_username}"(encryption_key, encryption_value) VALUES(?,?)', (key_letter[0], key_letter[1]))
                                print(letter_remover.LetterFunctions.letter_remover(random_generated_string))
                                encryption_key_cursor.execute(f'SELECT * FROM "{input_username}"')
                                encrypt_demo = encryption_key_cursor.fetchall()
                                encrypt1 = database_to_dict.database_to_dict(encrypt_demo)
                                encryption_key_db_connection.commit()
                                print("Encryption key was generated and was added as a key...")
                                return encrypt1, accept_checker
                            else:
                                accept_checker = False
                                return False, accept_checker          
                        if user_request == "n":
                            loger_checker = login_random_key_generation()
                            if loger_checker[1] != False:
                                encrypt1 = loger_checker[0]
                                accept_checker = True
                            elif loger_checker[1] == False:
                                accept_checker = False
                    if trial_times > 4:
                        print("you have no enrcyption key!! add one via config menu...")
                    # user encryption key fething form the database 
                    else:
                        encryption_key_cursor.execute(f'SELECT * FROM "{input_username}"')
                        db_global_user_encryption_key = encryption_key_cursor.fetchall()
                        global_user_encryption_key = letter_remover.LetterFunctions.letter_remover(database_to_string.database_to_string(db_global_user_encryption_key))
                        encrypt1 = database_to_dict.database_to_dict(db_global_user_encryption_key)           
                        Decrypter  = {value: key for key, value in encrypt1.items()}
                    while True:
                        user_input = input('> ')
                        user_covert_input = list(user_input)
                        return_list = []
                        if user_input == "/exit":
                            return
                        if user_input == "/logout":
                            break        
                        # config menu setting
                        if user_input.lower() == "/config":
                            user_request= input(CLI.EnDek_config_logo())
                            # Encryption Settings menu
                            if user_request == "1":
                                user_request_1 = CLI.EnDek_encyption_settings_menu()
                                # input for custom encryption key
                                if user_request_1 == "1":
                                    pre_user_encryption_key = input("key: ")
                                    user_encryption_key = list(pre_user_encryption_key)
                                    if len(user_encryption_key) != 0:
                                        # with scrambler 
                                        if user_encryption_key[-1] == "S":
                                            user_db_cursor.execute("UPDATE users SET scrambler = ? WHERE username = ? " , (True, input_username))
                                            unscrambler_key = input("Scrambler Key: ")
                                            user_encryption_key_unscrambled = new_encryption_key_unscrambler(scrambeled_encryption_key = pre_user_encryption_key, unscrambler = unscrambler_key , username = input_username)
                                            user_encryption_key_unscrambled = letter_remover.LetterFunctions.letter_adder(user_encryption_key_unscrambled)
                                            encryption_key_cursor.execute(f'DELETE FROM "{input_username}"')
                                            updated_encryption_key = twod_list_maker.list_maker(user_encryption_key_unscrambled)
                                            for key in updated_encryption_key:
                                                encryption_key_cursor.execute(f'INSERT INTO "{input_username}"( encryption_key , encryption_value) VALUES(?,?)', (key[0] , key[1]))
                                            print("Encryption key updated sucessfully...")
                                            encryption_key_cursor.execute(f'SELECT * FROM "{input_username}"')
                                            encrypt_demo = encryption_key_cursor.fetchall()
                                            encrypt1 = database_to_dict.database_to_dict(encrypt_demo)
                                            Decrypter  = {value: key for key, value in encrypt1.items()}
                                            encryption_key_db_connection.commit()
                                            user_db_connection.commit()
                                        #without scrambler 
                                        elif user_encryption_key[-1] != "S":
                                            encryption_key_cursor.execute(f'DELETE FROM "{input_username}"')
                                            updated_encryption_key = twod_list_maker.list_maker(user_encryption_key)
                                            for key in updated_encryption_key:
                                                encryption_key_cursor.execute(f'INSERT INTO "{input_username}"( encryption_key , encryption_value) VALUES(?,?)', (key[0] , key[1]))
                                            print("Encryption key updated sucessfully...")
                                            encryption_key_cursor.execute(f'SELECT * FROM "{input_username}"')
                                            encrypt_demo = encryption_key_cursor.fetchall()
                                            encrypt1 = database_to_dict.database_to_dict(encrypt_demo)
                                            Decrypter  = {value: key for key, value in encrypt1.items()}
                                            encryption_key_db_connection.commit()
                                    elif len(user_encryption_key) == 0:
                                        print("Encryption key cannot be empty...")
                                #Generate Secure Random Key menu
                                elif user_request_1 == "2":
                                    user_random_generation_agreement = input("Would you like to generate a random Encryption key(y/n): ")
                                    if user_random_generation_agreement == "y":
                                        is_using_srambler  = user_db_cursor.execute(f'SELECT scrambler FROM users WHERE username = ?' , (input_username,)).fetchone()[0]
                                        # generating random encryption with scramblers
                                        if is_using_srambler == 1:
                                            encryption_key_cursor.execute(f'DELETE FROM "{input_username}"')
                                            random_generated_string = randomgenerator()
                                            random_generated_list = twod_list_maker.list_maker(random_generated_string)
                                            for key_letter in random_generated_list:
                                                encryption_key_cursor.execute(f'INSERT INTO "{input_username}"(encryption_key, encryption_value) VALUES(?,?)', (key_letter[0], key_letter[1]))
                                            random_generated_string_full = letter_remover.LetterFunctions.letter_remover(random_generated_string)
                                            scrambled_encyption_key_output = pre_scrambler(random_generated_string_full, input_username)
                                            print(scrambled_encyption_key_output[0])
                                            print(scrambled_encyption_key_output[1])
                                            encryption_key_cursor.execute(f'SELECT * FROM "{input_username}"')
                                            encrypt_demo = encryption_key_cursor.fetchall()
                                            encrypt1 = database_to_dict.database_to_dict(encrypt_demo)
                                            Decrypter  = {value: key for key, value in encrypt1.items()}
                                            encryption_key_db_connection.commit()
                                            print("Encryption key was generated and was added as a key...")
                                        # generating random encryption without scramblers
                                        elif is_using_srambler == 0:
                                            random_generated_string = randomgenerator()
                                            random_generated_list = twod_list_maker.list_maker(random_generated_string)
                                            encryption_key_cursor.execute(f'DELETE FROM "{input_username}"')
                                            for key_letter in random_generated_list:
                                                encryption_key_cursor.execute(f'INSERT INTO "{input_username}"(encryption_key, encryption_value) VALUES(?,?)', (key_letter[0], key_letter[1]))
                                            random_generated_string_full = letter_remover.LetterFunctions.letter_remover(random_generated_string)
                                            print(random_generated_string_full)
                                            encryption_key_cursor.execute(f'SELECT * FROM "{input_username}"')
                                            encrypt_demo = encryption_key_cursor.fetchall()
                                            encrypt1 = database_to_dict.database_to_dict(encrypt_demo)
                                            Decrypter  = {value: key for key, value in encrypt1.items()}
                                            encryption_key_db_connection.commit()
                                            print("Encryption key was generated and was added as a key...")
                                # Database Settings menu
                                elif user_request_1 == "3":
                                    user_db_cursor.execute("SELECT scrambler FROM users WHERE username = ? " , (input_username,))
                                    scrambler_status = user_db_cursor.fetchone()[0]
                                    if scrambler_status == 1:
                                        user_request_for_pre_scrambler = CLI.Scramble_settings_menu()
                                        if user_request_for_pre_scrambler == "1":
                                            scrambler_changer_user_request = CLI.new_Scramble_settings_menu()
                                            if scrambler_changer_user_request == "1":
                                                scrambler_key_new = CLI.new_Scramble_key_for_pre_user()
                                                if len(scrambler_key_new) == 0:
                                                    print("Encryption key cannot be empty...")
                                                else:
                                                    new_encryption_scrambler = scrambeler_updater(scrambler_key= scrambler_key_new, username = input_username)
                                                    print("Scrambler key updated successfully...")
                                            elif scrambler_changer_user_request == "2":
                                                new_encryption_scrambler = scrambler(Encryption_key = global_user_encryption_key, username = input_username)
                                                print("Encryption key updated successfully...")
                                                print("New Scrambler key: " + str(new_encryption_scrambler[1]))
                                        elif user_request_for_pre_scrambler == "2":
                                            user_db_cursor.execute("UPDATE users SET scrambler = ? WHERE username = ? " , (False, input_username))
                                            user_db_connection.commit()
                                    elif scrambler_status == 0 or scrambler_status is None:
                                        user_request_scrambler = CLI.first_Scramble_settings_menu()
                                        if user_request_scrambler == "1":
                                            user_db_cursor.execute("UPDATE users SET scrambler = ? WHERE username = ? " , (True, input_username))
                                            user_db_connection.commit()
                                            encryption_key_cursor.execute(f'SELECT * FROM "{input_username}"')
                                            scrambler_encryption_key = encryption_key_cursor.fetchall()
                                            scrambler_encryption_key_2 = letter_remover.LetterFunctions.letter_remover(database_to_string.database_to_string(scrambler_encryption_key))
                                            scrambled_encyption_key_output = scrambler(scrambler_encryption_key_2, input_username)
                                            print(scrambled_encyption_key_output[0])
                                            print(scrambled_encyption_key_output[1])
                                elif user_request_1 == "4":
                                    user_database_security = getpass.getpass("sudo: ")
                                    if password_verification(user_database_security, users[input_username]):
                                        encryption_key_cursor.execute(f'SELECT * FROM "{input_username}"')
                                        encrypt_demo = encryption_key_cursor.fetchall() 
                                        if len(encrypt_demo) == 0:
                                            print("No encryption key found...")
                                        elif len(encrypt_demo) != 0:
                                            is_using_srambler  = user_db_cursor.execute(f'SELECT scrambler FROM users WHERE username = ?' , (input_username,)).fetchone()[0]
                                            if is_using_srambler == 1:
                                                pre_returned_string = database_to_string.database_to_string(encrypt_demo)
                                                returned_string = letter_remover.LetterFunctions.letter_remover(pre_returned_string)
                                                final_returned_string = pre_scrambler(returned_string, input_username)
                                                print("Encryption key: " + str(final_returned_string[0]))
                                                print("Scrambler key: " + str(final_returned_string[1]))
                                                print("Encryption key and Scrambler key exported successfully...")
                                            elif is_using_srambler == 0:
                                                pre_returned_string = database_to_string.database_to_string(encrypt_demo)
                                                returned_string = letter_remover.LetterFunctions.letter_remover(pre_returned_string)
                                                print("Encryption key: " + returned_string)
                                                print("Encryption key exported successfully...")
                            elif user_request == "3":
                                user_request_3 = CLI.Database_settings_menu()
                                if user_request_3 == "1":
                                    encryption_key_cursor.execute(f'DELETE FROM "{input_username}"')
                                    encryption_key_cursor.execute(f'DROP TABLE "{input_username}"')
                                    encryption_key_db_connection.commit()
                                    encryption_key_db_connection.close()
                                    print("DataBase is clear")
                                    encryption_key_cursor.execute(f'SELECT * FROM "{input_username}"') 
                                    encrypt_demo = encryption_key_cursor.fetchall()
                                    user_panic(input_username)
                                    encrypt1 = database_to_dict.database_to_dict(encrypt_demo)
                                    Decrypter  = {value: key for key, value in encrypt1.items()}
                                    if __name__ == "__main__":
                                        main()
                                    return
                            elif user_request == "2":
                                user_request_2 = CLI.Account_settings_menu()
                                if user_request_2 == "2":
                                    conformation = CLI.Account_confirmation_menu()
                                    if conformation == "1":
                                        encryption_key_cursor.execute(f'DELETE FROM "{input_username}"')
                                        encryption_key_db_connection.commit()
                                        is_using_srambler  = user_db_cursor.execute(f'SELECT scrambler FROM users WHERE username = ?' , (input_username,)).fetchone()[0]
                                        if is_using_srambler == 1:
                                            user_panic(input_username)
                                        user_db_cursor.execute(f'DELETE FROM users WHERE username = (?)', (input_username,))
                                        user_db_connection.commit()
                                        user_db_cursor.execute("SELECT * FROM users ")
                                        users = database_to_dict.database_to_dict(user_db_cursor.fetchall())
                                        encrypt_demo = encryption_key_cursor.fetchall()
                                        encrypt1 = database_to_dict.database_to_dict(encrypt_demo)
                                        Decrypter  = {value: key for key, value in encrypt1.items()}
                                        raise AccoutDeletion()                                       
                                elif user_request_2 == "1":
                                    break
                            elif user_request == "4":
                                user_request_dual_endek = CLI.endek_dual_settings()
                                if user_request_dual_endek == "1":
                                    CLI.logos()
                                    print("Version " + EnDek_verison)
                                    print("Encryption key status: currently running")
                                    user_db_cursor.execute("SELECT * FROM users ")
                                    users_number = len(user_db_cursor.fetchall())
                                    if users_number != 1:
                                        print(f"There are {users_number} local users.")
                                    else:
                                        print("There is 1 local user.")
                                    is_using_srambler  = user_db_cursor.execute(f'SELECT scrambler FROM users WHERE username = ?' , (input_username,)).fetchone()[0]
                                    if is_using_srambler == 1:
                                        print("Scrambler status: Enabled")
                                    elif is_using_srambler == 0:
                                        print("Scrambler status: Disabled")
                                elif user_request_dual_endek == "2":
                                    print(updater.update_checker(EnDek_verison))
                                    
                                
                        if len(user_covert_input) !=0 :
                            if user_covert_input[-1] == "E" and user_input !="/config":
                                encryption_key_cursor.execute(f'SELECT * FROM "{input_username}"')
                                encrypt_demo = encryption_key_cursor.fetchall()
                                encrypt = database_to_dict.database_to_dict(encrypt_demo)
                                Decrypter  = {value: key for key, value in encrypt1.items()}
                                for i in user_covert_input:
                                    if i in Decrypter:
                                        return_list.append(Decrypter.get(i , "letter not found :("))
                                return_word = "". join(return_list)
                                print(return_word)
                            if user_covert_input[-1] != "E" and user_input !="/config":
                                for i in user_covert_input :
                                    try:
                                        return_list.append(encrypt1[i])               
                                        if len(user_covert_input) == len(return_list):
                                            return_list.append("E")
                                            return_sentence = "". join(return_list)
                                            print(return_sentence)
                                    except KeyError:
                                        print("invalid character: " + i)
                    user_db_connection.close()
                    encryption_key_db_connection.close()
                       
                except AccoutDeletion:
                    print("account deleted sucessfully...")
                except KeyboardInterrupt:
                    print("Thank You for using EnDek")
                    return
                except Exception as e:
                    print(f"error occured: {e}")
                    print("if you were trying to enter any kind of input, please make sure it is a valid Type of input in EnDek")
            except KeyboardInterrupt:
                print("Thank You for using EnDek")
                return
            except Exception as e:
                print(f"An error occurred while fetching encryption keys: {e}")
        elif input_username not in users:
            new_user = input("user not found. would you like to create a new user(y/n): ")
            if new_user == "y":
                new_user_password = password_hashing(getpass.getpass("password: "))
                recheck = getpass.getpass("Re-enter password: ")
                if password_verification(recheck, new_user_password):
                    user_db_cursor.execute("INSERT INTO users(username, password, scrambler) VALUES(?, ?, ?)", (input_username, new_user_password, False))
                    user_db_connection.commit()
                    print("user created successfully...")
                else:
                    print("passwords do not match!!")

            elif new_user == "n":
                user_reponse = input("Do you have an encryption key(y/n): ")
                if user_reponse == "y":
                    key_before = input("Key: ")
                    if key_before[-1] == "S":
                        print("you cannot decrypt without a siging in.")
                    elif key_before[-1] != "S":
                        key = letter_remover.LetterFunctions.letter_adder(key_before)
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
                        key_after = letter_remover.LetterFunctions.letter_remover(key)
                        print(key_after)
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

if __name__ == "__main__":
    main()