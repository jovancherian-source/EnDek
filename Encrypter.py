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
        for i in final_before_encrypt_lsit:
                return_list.append(encrypt1[i])
        return_sentence = "" . join(return_list)
        print(return_sentence)