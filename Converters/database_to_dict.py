return_list = []
return_dict = {}
def database_to_dict(input_list):
    try:
        for i in input_list:
            return_list.append(list(i))
        for item in return_list:
            return_dict[item[0]] = item[1]
        return return_dict
    except IndexError:
        print("Invalid encryption key Format ")
        return False