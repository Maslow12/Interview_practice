def drop_duplicates(arr,cleansed=[]):
    for i in arr:
        if i not in cleansed:
            cleansed.append(i)
    return cleansed
    
def revalid(s):
    pass
def isValid(s):
    arr = []
    for i in drop_duplicates(s):
        arr.append(s.count(i))
    if len(set(arr))==1:   
        st = 'YES'
    else:
        st = 'NO'
        return arr
    return st