def to_encrypt(text, delta):
    list_text = list(text)
    print("a:",ord("a"),"z:",ord("z"))
    print("A:",ord("A"),"Z:",ord("Z"))
    print(ord("`"))
    for index,item in enumerate(list_text):
        if 96 < ord(item) < 123:
            list_text[index] = chr((ord(item) - 97 + delta)%26 + 97)
        if 64 < ord(item) < 91:
            list_text[index] = chr((ord(item) - 65 + delta)%26 + 65)
    text = "".join(list_text)
    return text

def to_decrypt(text, delta):
    list_text = list(text)
    print("a:",ord("a"),"z:",ord("z"))
    print("A:",ord("A"),"Z:",ord("Z"))
    print(ord("`"))
    for index,item in enumerate(list_text):
        if 96 < ord(item) < 123:
            list_text[index] = chr((ord(item) - 97 + delta)%26 + 97)
        if 64 < ord(item) < 91:
            list_text[index] = chr((ord(item) - 65 + delta)%26 + 65)
    text = "".join(list_text)
    return text

text = "abcdefghijklmnopqrstuvwxyz"
delta = -1

text = to_encrypt(text,delta)
print(text)
print(to_decrypt(text,delta*-1))
