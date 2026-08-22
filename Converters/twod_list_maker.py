def list_maker(input_string):
    try:
        one_d_list = list(input_string)
        two_d_list = []
        for item in range(0 ,len(one_d_list), 2):
            two_d_list.append([one_d_list[item], one_d_list[item+1]])
        return two_d_list
    except IndexError:
        print("Invalid encryption key Format ")
        return False