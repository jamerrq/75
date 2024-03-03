from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        min_so_far = [0] * n
        max_so_far = [0] * n
        for i in range(n):
            numi = nums[i]
            numj = nums[n - i - 1]
            if not i:
                min_so_far[0] = numi
                max_so_far[n - 1] = numj
                continue
            min_so_far[i] = min(numi, min_so_far[i - 1])
            max_so_far[-i-1] = max(numj, max_so_far[-i])

        for i in range(1, n - 1):
            if min_so_far[i-1] < nums[i] < max_so_far[i+1]:
                return True

        return False
