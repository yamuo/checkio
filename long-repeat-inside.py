import copy

def repeat_inside(line):
    ret_can = [""]
    
    for i in range(len(line)):
        for j in range(1,(len(line)-i+1)//2):
            k = copy.deepcopy(i)
            pre = None
            repeat = None
            while k < len(line) :
                if pre == None:
                    pre = line[k:k+j]
                    repeat = line[k:k+j]
                elif pre == line[k:k+j]:
                    #print(pre,"==",line[k:k+j])
                    pre = line[k:k+j]
                    repeat += line[k:k+j]
                    ret_can.append(repeat)
                    #print(repeat)
                else:
                    pre = line[k:k+j]
                    repeat = line[k:k+j]
                k += j
                
    return max(ret_can,key=len)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert repeat_inside('aaaaa') == 'aaaaa', "First"
    assert repeat_inside('aabbff') == 'aa', "Second"
    assert repeat_inside('aababcc') == 'abab', "Third"
    assert repeat_inside('abc') == '', "Forth"
    assert repeat_inside('abcabcabab') == 'abcabc', "Fifth"
    print('"Run" is good. How is "Check"?')