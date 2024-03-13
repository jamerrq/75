from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        prev = None
        while head:
            tmp = head.next
            if prev:
                head.next = prev
            else:
                head.next = None
            prev = head
            head = tmp

        return prev
