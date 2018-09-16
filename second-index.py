def second_index(text: str, symbol: str) -> [int, None]:
    count = 0
    for i,v in enumerate(text):
        if v == symbol and count == 1:
            return i
        elif v == symbol and count == 0:
            count += 1
    return None
