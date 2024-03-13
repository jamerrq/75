from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: return head
        even = None
        oddh = None
        first_odd = None
        first_even = None
        indx = 0
        while head is not None:
            if indx % 2:
                if oddh is None:
                    oddh = head
                    first_odd = oddh
                else:
                    oddh.next = head
                    oddh = oddh.next
            else:
                if even is None:
                    even = head
                    first_even = even
                else:
                    even.next = head
                    even = even.next

            head = head.next
            indx += 1

        if oddh:
            oddh.next = None
            even.next = first_odd

        return first_even
