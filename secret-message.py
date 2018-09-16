def find_message(text: str) -> str:
    
    ret = ""
    
    for i in text:
        if i.isupper():
            ret += i
            
    return ret
