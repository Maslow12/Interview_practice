 # Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
    
def solution(l):
    head = None
    node = l
    head = node
    arr = []
    while head:
        arr.append(head.value)
        head = head.next
    arr_2 = []
    prev = None
    current = head
    while current:
        after = current.next
        nex = after
        prev = after
        after = current
        current = nex
        arr_2.append = prev.value
    
    if arr == arr[::-1]:
        return True
    return False
        