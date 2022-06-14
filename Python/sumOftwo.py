import numpy as np
def solution(a, b, v):
    a,b = np.array(a),np.array(b)
    for i in range(len(b)):
        if v-b[i] in a:
            return True
    return False
