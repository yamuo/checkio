def non_repeat(line):
    line_len = len(line)
    ret_can = [""]
    
    for i,v in enumerate(line):
        exist = []
        ret = []
        for j in range(i ,line_len):
            if line[j] not in exist: 
                ret.append(line[j])
                exist.append(line[j])
                ret_can.append("".join(ret))
            else:
                ret_can.append("".join(ret))
                break
    
    
    return max(ret_can, key=len)


print(non_repeat('agqiwuhsgpr'))