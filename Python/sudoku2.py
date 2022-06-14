import numpy as np
from collections import Counter

def solution(grid):
    for i in range(len(grid[0])):
        a = np.array(grid, dtype=str)[i:i+1,:]
        b = np.array(grid, dtype=str)[:,i:i+1].reshape(1,-1)
        for k1,v1 in zip(np.unique(a, return_counts=True)[0],np.unique(a, return_counts=True)[1]):
            if v1 > 1 and k1 != '.' or m3x(grid):
                return False
        for k2,v2 in zip(np.unique(b,return_counts=True)[0], np.unique(b,return_counts=True)[1]):
            if v2 > 1 and k2 != '.':
                return False
    return True 
            
def m3x(grid):
    a = np.array(grid)
    for i in range(0,8,3):
        for j in range(0,8,3):
            for k,v in zip(np.unique(a[i:i+3,j:j+3], return_counts=True)[0], np.unique(a[i:i+3,j:j+3], return_counts=True)[1]):
                if int(v)>1 and k!='.':
                    return True
    return False
    