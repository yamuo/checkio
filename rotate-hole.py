def rotate(state, pipe_numbers):
    ret = []
    count = 0
    for k in range(len(state)):
        for i,v in enumerate(pipe_numbers):
            if state[v] !=1 :
                break
            
            if i+1 == len(pipe_numbers):
                ret.append(count)       
                
        state = role(state)
        count += 1
    
    return ret
                

def role(in_list):
    ret = []
    
    for i,v in enumerate(in_list):
        try :
            ret.append(in_list[i-1])
        except :
            ret.append(in_list[-1])
        
    return ret
        

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1]) == [1, 8], "Example"
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1, 2]) == [], "Mission impossible"
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1], [0, 4, 5]) == [0], "Don't touch it"
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1], [5, 4, 5]) == [0, 5], "Two cannonballs in the same pipe"
