#If the wheel is already created, why reinvent it?
import numpy as np
def solution(a):
    return np.rot90(a,k=3)