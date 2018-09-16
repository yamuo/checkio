def easy_unpack(elements: tuple) -> tuple:
    elemants_list = list(elements)
    ret = []
    
    ret.append(elemants_list[0])
    ret.append(elemants_list[2])
    ret.append(elemants_list[-2])
    
    return tuple(ret)
