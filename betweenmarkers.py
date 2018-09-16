def between_markers(text: str, begin: str, end: str) -> str:
    ret = ""
    
    if text.find(begin) >= 0:
        if text.find(begin) < text.find(end)  :
            return text[text.find(begin)+len(begin):text.find(end)]
        elif text.find(end) == -1:
            return text[text.find(begin)+len(begin):]
    elif text.find(end) >= 0:
        return text[0:text.find(end)]
    elif text.find(begin) == text.find(end) == -1:
        return text
    
    return ret