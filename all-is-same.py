from typing import List, Any

def all_the_same(elements: List[Any]) -> bool:
    pre_c = None
    current_c = None
    result = True
    for i in elements:
        if pre_c == None:
            pre_c = i
        elif pre_c != i:
            result = False
        pre_c = i
            
    return result

print(all_the_same(["a","a","a","b","a","a"]))
