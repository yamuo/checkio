def say_hi(name: str, age: int) -> str:
    return "{0}{1}{2}{3}{4}".format("Hi. My name is ",name," and I'm ",age," years old")

print(say_hi("Alex", 32))

"""
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", "First"
    assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", "Second"
    print('Done. Time to Check.')
"""