def count_words(str,set):
    set_list = [*set]
    str = str.lower()
    count = 0
    for i in set_list:
        str = str.replace(i.lower(), "¥", 1)
        print(i)
        print(str)
    
    return str.count("¥")

print(count_words("Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.",["far","word","vokal","count","tries"]))
