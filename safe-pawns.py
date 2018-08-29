def safe_pawns(pawns: set) -> int:
    pawns = list(pawns)
    list_pawns = []
    safe_point = []
    for i in pawns:
        list_pawns.append(list(i))
        safe_point.append(chr(ord(list(i)[0])+1) + str(int(list(i)[1])+1))
        safe_point.append(chr(ord(list(i)[0])-1) + str(int(list(i)[1])+1))

    safe_point = list(set(pawns) & set(safe_point))

    return len(safe_point)


pawns = {"b4", "d4", "f4", "c3", "e3", "g5", "d2"}
print(safe_pawns(pawns))

