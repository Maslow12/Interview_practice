def solution(n):
    th1,th2,arr,s,count=0,1,[],0,1
    for i in range(n+2):    
        arr.append(s)
        th1=th2
        th2=s
        s=th1+th2
    return arr[len(arr)-1]

# Is a Fibonnaci Serie