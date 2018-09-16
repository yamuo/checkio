def checkio(number: int) -> int:
    ret = 1
    for i in str(number):
        if int(i) != 0:   
            ret = ret * int(i)
    
    return ret
