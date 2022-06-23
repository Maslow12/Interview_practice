# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def solution(l, k):
    node = l
    head = node
    arr = []
    while head:
        arr.append(head.value)
        head = head.next
    arr = revbyK(arr,k)
    
    return arr
    
    
def revbyK(arr,k):
    for i in range(0,len(arr)-k+1,k):
        r = arr[i:i+k]
        r.reverse()
        arr[i:i+k] = r
    return arr
