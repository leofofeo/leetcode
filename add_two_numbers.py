# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        pass
    
def reverse_li(li):
    val = []
    curr_li = li
    next_is_not_none = True
    while next_is_not_none:
        val.append(curr_li.val)
        if curr_li.next is None:
            next_is_not_none = False
        else:
            curr_li = curr_li.next
            
    return val