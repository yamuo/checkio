def checkio(input):
    input_list = list(str(input))
    len_list = len(input_list)
    
    for i,v in enumerate(input_list):
        digit = len_list - i
        v = int(v)
        if digit == 4:
            input_list[i] = "M" * v
        if digit == 3:
            if v <= 3 :
                input_list[i] = "C" * v   
            if v == 4 :
                input_list[i] = "CD"
            if 8 >= v >= 5 :
                input_list[i] = "D" + "C" * (v - 5)
            if v == 9:
                input_list[i] = "CM"
                
        if digit == 2:
            if v <= 3 :
                input_list[i] = "X" * v   
            if v == 4 :
                input_list[i] = "XL"
            if 8 >= v >= 5 :
                input_list[i] = "L" + "X" * (v - 5) 
            if v == 9:
                input_list[i] = "XC"
                
                            
        if digit == 1:
            if v <= 3 :
                input_list[i] = "I" * v   
            if v == 4 :
                input_list[i] = "IV"
            if 8 >= v >= 5 :
                input_list[i] = "V" + "I" * (v - 5) 
            if v == 9:
                input_list[i] = "IX"
        
    ret = ''.join(input_list)

    return ret

i = 3999
print(checkio(i))