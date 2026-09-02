class LetterFunctions():
    def letter_remover(input_string):
        try:
            input_list = list(input_string)
            final_list = []
            for i in range(1 ,len(input_list), 2):
                if i < len(input_list):
                    final_list.append(input_list[i])
            return "".join(final_list)
        except IndexError:
            print("Invalid encryption key Format ")
            return False
    def letter_adder(input_string):
        try:
            input_list = list(input_string)
            for item in input_list:
                if item == " ":
                    input_list.remove(item)
            final_list = []
            letters = ['a','b', 'c', 'd', 'e' ,'f', 'g' ,'h','i', 'j', 'k', 'l' , 'm' , 'n', 'o', 'p', 'q' , 'r', 's' ,'t', 'u' ," ", 'v', 'w', 'x', 'y', 'z', '.' ]
            for i in range(0 ,len(input_list)):
                if i < len(input_list):
                    final_list.append(letters[i])
                    final_list.append(input_list[i])
            return "".join(final_list)
        except IndexError:
            print("Invalid encryption key Format ")
            return False