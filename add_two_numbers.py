# Definition for singly-linked list.
import sys
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        val_1 = concat_li_values(reverse_li(l1))
        val_2 = concat_li_values(reverse_li(l2))

        return extract_li_values(val_1 + val_2)

    
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

def concat_li_values(arr: list) -> int:
    return int(''.join(str(v) for v in arr))

def extract_li_values(sum: int) -> ListNode:
    # take int and turn it into single digits and split into list
    sum_list = [ListNode(int(d)) for d in str(sum)]
    sum_list = sum_list[::-1]
    for idx, val in enumerate(sum_list):
        if idx == len(sum_list) - 1:
            continue
        val.next = sum_list[idx + 1]
    return sum_list[0]
