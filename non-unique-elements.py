def del_unique(list):
    list_dict = {}
    list_dup = []
    for i in list:
        if not i in list_dict:
            list_dict[i] = 1
        elif i in list_dict:
            list_dict[i] += 1

    for i in list:
        if list_dict[i] >= 2:
            list_dup.append(i)
            
    return list_dup

print(del_unique([1,2,3,4,5,6,7,8,9,1,2,3,4,5]))
