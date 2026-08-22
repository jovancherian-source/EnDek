def database_to_string(input_2d_list):
    try:
        return_list = []
        for i in input_2d_list:
            return_list.append(i[0])
            return_list.append(i[1])
        return "".join(return_list)
    except IndexError:
        print("Invalid encryption key Format ")
        return False