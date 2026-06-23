users = ["jovancherian"]
password = '3e3e3e'

encrypt1 = {
    'a' : '✈',
    'b': '[',
    'c' : '✖',
    'd': '✍',
    'e' : '☁',
    'f': '¥',
    'g': '®',
    'h': '□',
    'i' : '▼',
    'j' : '∇',
    'k' : '☀',
    'l' : 'λ',
    'm': '☆',
    'n': '✧',
    'o': '✎',
    'p' : 'θ',
    'q' : ']',
    'r' : '₹',
    's' : '⌨',
    't' : '▽',
    'u' : '☕',
    'v' : '$',
    'w' : '⚙',
    'x' : '@',
    'y': '%',
    'z' : '△',
    ' ' : ' '

}

input_username = input("username: ")

if input_username in users:
    input_password_1 = input("sudo: ")
    while input_password_1 == password:
        user_input = input('> ')
        final_before_encrypt_lsit = list(user_input)
        return_list = []
        if user_input == "exit":
             break
        for i in final_before_encrypt_lsit:
                try:
                    return_list.append(encrypt1[i])               
                    return_sentence = "" . join(return_list)
                    if len(final_before_encrypt_lsit) == len(list(return_sentence)):
                        print(return_sentence)
                except KeyError:
                    print("invalid characters")
    if input_password_1 != password:
         print("wrong password!!")              
elif input_username not in users:
     user_reponse = input("user not found.Do you have and encrypt password(y/n)")
     if user_reponse == "y":
        uknown_user_password = input("sudo: ")
        x = 0
        while uknown_user_password == password and x < 5:
                x += 1
                user_input = input('> ')
                final_before_encrypt_lsit = list(user_input)
                return_list = []
                if user_input == "exit":
                     break
                for i in final_before_encrypt_lsit:
                    try:
                        return_list.append(encrypt1[i])               
                        return_sentence = "" . join(return_list)
                        if len(final_before_encrypt_lsit) == len(list(return_sentence)):
                            print(return_sentence)
                    except KeyError:
                        print("invalid characters")
        if uknown_user_password != password:
            print("wrong password!")
          
               
     