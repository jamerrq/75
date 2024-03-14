from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)

        for num in nums[k:]:
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)

        return heap[0]


# Alternative O(n)
"""
class Solution:
def findKthLargest(self, nums: List[int], k: int) -> int:
    return sorted(nums, reverse=True)[k - 1]
"""
