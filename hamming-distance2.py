def checkio(n, m):
    n = str(format(n, 'b'))
    m = str(format(m, 'b'))
    max_input = max(len(n),len(m))
    n = n.zfill(max_input)
    m = m.zfill(max_input)
    count = 0
    
    for i in range(max_input):
        if n[i] != m[i]:
            count += 1
    
    return count



print(checkio(117, 17))