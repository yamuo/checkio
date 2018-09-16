def checkio(words: str) -> bool:
    ret = False
    count = 0
    
    for i in words.split():
        if i.isalpha():
            count += 1
            if count == 3:
                return True
        else:
            count = 0
    
    return ret
