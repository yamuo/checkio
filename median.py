from typing import List
import math

def checkio(data: List[int]) -> [int, float]:
    data.sort()
    half_len = len(data) / 2
    ret = 0
    
    if half_len%1 == 0:
        half_len = int(half_len)
        ret = (data[half_len - 1] + data[half_len]) / 2
    else:
        ret = data[math.ceil(half_len) - 1]
        
    return ret

print(checkio(list(range(1000000))))