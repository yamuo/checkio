def checkio(array):
    ret = 0
    try:
        for i,v in enumerate(array):
            if i%2 == 0 :
                ret += v
                
        return ret * array[-1]
    except:
        return ret
            