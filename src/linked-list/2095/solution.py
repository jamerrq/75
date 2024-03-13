from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        ref_head = head
        tmp = head
        while tmp:
            count += 1
            tmp = tmp.next

        mid = count // 2
        ind = 0
        tmp = ref_head
        prev = None
        while tmp:
            if ind == mid:
                if prev:
                    prev.next = tmp.next
                else:
                    ref_head = tmp.next
                break
            else:
                prev = tmp
                tmp = tmp.next
                ind += 1

        return ref_head
