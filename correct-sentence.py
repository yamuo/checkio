def correct_sentence(text: str) -> str:
    if text[-1] == ".":
        return text[0].upper() + text[1:] 
    else:
        return text[0].upper() + text[1:] + "."
