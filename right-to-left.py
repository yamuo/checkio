def left_join(phrases):
    list_phrases = list(phrases)
    
    for i,v in enumerate(list_phrases):
        list_phrases[i] = v.replace('right', 'left')
    
    return ",".join(list_phrases)
