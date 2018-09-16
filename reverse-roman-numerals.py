from collections import Counter

def reverse_roman(roman_string):
    roman_dict = Counter(roman_string)
    ret = 0
    roman = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    
    for i,v in enumerate(roman_string):
        
        if i == 0:
            ret += roman[roman_string[-(i+1)]]
        elif roman[roman_string[-(i+1)]] < roman[roman_string[-(i)]]:
            ret -= roman[roman_string[-(i+1)]]
        else :
            ret += roman[roman_string[-(i+1)]]
            
    return ret


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert reverse_roman('VI') == 6, '6'
    assert reverse_roman('LXXVI') == 76, '76'
    assert reverse_roman('CDXCIX') == 499, '499'
    assert reverse_roman('MMMDCCCLXXXVIII') == 3888, '3888'
    print('Great! It is time to Check your code!');
