from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        n = 0
        vals = []
        #
        while head:
            vals.append(head.val)
            head = head.next
            n += 1
            continue
        #
        ans = 0
        for i in range(n // 2):
            ans = max(ans, vals[i] + vals[n - i - 1])

        return ans
