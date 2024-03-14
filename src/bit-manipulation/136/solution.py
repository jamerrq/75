from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        single = nums[0]
        if n > 1 and nums[0] != nums[1]:
            pass
        elif n > 1:
            if nums[-1] != nums[-2]:
                single = nums[-1]
            else:
                for i in range(1, n - 1):
                    if nums[i] != nums[i - 1] and nums[i] != nums[i + 1]:
                        single = nums[i]
                        break
        return single
