def splash():
    orange = "\033[38;5;214m"
    reset = "\033[0m"

    print(orange)

    print(r"""
  ███████╗        
  ██╔════╝      ██████╗       ██╗  ██╗
  ██║    _ __   ██╔══██╗      ██║ ██╔╝
  █████╗| '_ \  ██║  ██║/ _ \ ██╠═██╔╝
  ██╔══╝| | | | ██║  ██║  __/ ██║╚██╗ 
  ██║   |_| |_| ██████╔╝\___| ██║ ╚██╗
  ███████╗      ╚═════╝       ╚═╝  ╚═╝
                 EnDek
    """)

    print(reset)

splash()

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

Decrypter = { v : k for k, v in encrypt1.items()}

input_username = input("username: ")

if input_username in users:
    input_password_1 = input("sudo: ")
    while input_password_1 == password:
        user_input = input('> ')
        user_covert_input = list(user_input)
        return_list = []
        if user_input == "exit":
             break
        if user_covert_input[-1] == "E":
            for i in user_covert_input:
                if i in Decrypter:
                    return_list.append(Decrypter.get(i , "letter not found :("))
            return_word = "". join(return_list)
            print(return_word)
        if user_covert_input[-1] != "E":
            for i in user_covert_input :
                try:
                    return_list.append(encrypt1[i])               
                    if len(user_covert_input) == len(return_list):
                        return_list.append("E")
                        return_sentence = "". join(return_list)
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
                user_covert_input = list(user_input)
                return_list = []
                if user_input == "exit":
                     break
                for i in user_covert_input:
                    try:
                        return_list.append(encrypt1[i])               
                        return_sentence = "" . join(return_list)
                        if len(user_covert_input) == len(list(return_sentence)):
                            print(return_sentence)
                    except KeyError:
                        print("invalid characters")
        if uknown_user_password != password:
            print("wrong password!")
          
               
     