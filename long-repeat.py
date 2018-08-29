def long_repeat(line):
    pre_c = None
    current_c = None
    count = 1
    max_count = 0
    for i in line:
        if pre_c == None:
            pre_c = i
        elif pre_c == i:
            count += 1
            if max_count <= count:
                max_count = count
        elif pre_c != i:
            if max_count <= count:
                max_count = count
            count = 1
        pre_c = i
            
    return max_count

print(long_repeat("aaaaaa"))
