def uniq_add(my_list=[]):
    result = 0
    uniq_list = []
    for x in my_list:
        if x not in uniq_list:
            uniq_list.append(x)
            result += x
    return result
