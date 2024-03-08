from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1 = set(nums1)
        s2 = set(nums2)
        d1 = s1.difference(s2)
        d2 = s2.difference(s1)
        return [list(d1), list(d2)]
