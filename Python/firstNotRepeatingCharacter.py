from collections import Counter

def solution(s):
    k = Counter(s)
    for key,value in k.items():
        if value==1:
            return key
    return '_'