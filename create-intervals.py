def create_intervals(data):
    data_list = list(data)
    data_list.sort()
    print(data_list)
    ret = []
    interval = [0,0]
    j = 0
    for i,v in enumerate(data_list):
        print(i,v)
        if j == 0:
            interval[0] = v
        if i+1 < len(data_list):
            if data_list[i+1] == data_list[i]+1:
                interval[1] = data_list[i+1]
                j += 1
            else :
                j = 0
                interval[1] = data_list[i]
                ret.append(tuple(interval))
                print(interval)
        else:
            interval[1] = v
            print(interval)
            ret.append(tuple(interval))
        
    return ret

print(create_intervals({1, 2, 3, 4, 5, 7, 8, 12}))

"""
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert create_intervals({1, 2, 3, 4, 5, 7, 8, 12}) == [(1, 5), (7, 8), (12, 12)], "First"
    assert create_intervals({1, 2, 3, 6, 7, 8, 4, 5}) == [(1, 8)], "Second"
    print('Almost done! The only thing left to do is to Check it!')
"""