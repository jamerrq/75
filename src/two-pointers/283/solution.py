from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nz = sum([1 for x in nums if not x])
        nums[:] = [x for x in nums if x] + [0] * nz
