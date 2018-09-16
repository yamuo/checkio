from collections import Counter

def most_frequent(data: list) -> str:
    counter = Counter(data)
    return max(counter, key=counter.get)
