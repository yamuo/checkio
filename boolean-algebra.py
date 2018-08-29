OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")

def boolean(x, y, operation):
    ret = 0
    if operation == OPERATION_NAMES[0]:
        if x == y == 1:
            ret = 1
    
    if operation == OPERATION_NAMES[1]:
        if x == y == 0:
            ret = 0
        else:
            ret = 1
    
    if operation == OPERATION_NAMES[2]:
        if x == 1:
            ret = y
        else:
            ret = x
        
    if operation == OPERATION_NAMES[3]:
        ret = (x+y)%2
        
    if operation == OPERATION_NAMES[4]:
        if x == y:
            ret = 1
    
    return ret