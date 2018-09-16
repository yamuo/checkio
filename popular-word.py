def popular_words(text: str, words: list) -> dict:
    text = text.lower()
    text_list = text.split()
    ret = {}
    
    for n in words :
        ret[n] = text_list.count(n)  
    
    return ret
