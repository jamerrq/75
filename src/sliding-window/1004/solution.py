from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        #
        i, j, zs, os = [0] * 4
        #
        ans = 0
        n = len(nums)
        #
        while zs < k and j < n:
            numj = nums[j]
            if numj:
                os += 1
            else:
                zs += 1
            ans = max(ans, os + zs)
            j += 1
        #
        while j < n:
            numj = nums[j]
            if numj:
                os += 1
            else:
                zs += 1
                while zs > k:
                    numi = nums[i]
                    if numi:
                        os -= 1
                    else:
                        zs -= 1
                    i += 1
            ans = max(ans, os + zs)
            j += 1

        return ans
