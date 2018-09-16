VOWELS = "aeiouy"

def translate(phrase):
    v_count = 0
    ret = ""
    
    for i,v in enumerate(phrase):
        
        if i == 0:
            ret += v
        elif VOWELS.find(v) == -1 :
            ret += v
        elif VOWELS.find(phrase[i-1]) == -1 and phrase[i-1] == " ":
            v_count = 1
        elif VOWELS.find(phrase[i-1]) == -1:
            pass
        elif v_count != 3 :
            v_count += 1
            if v_count == 3 :
                ret += v
                v_count = 0
        
    return ret
