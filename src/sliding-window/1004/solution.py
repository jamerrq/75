from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start = 0
        end = 1
        zeros, ones = 0, 0
        if nums[0] == 1:
            ones = 1
            ans = 1
        else:
            if k:
                zeros = 1
                ans = 1
            else:
                start += 1
        ans = 0
        snd_zero = -1
        while end < len(nums):
            num = nums[end]
            if num:
                ones += 1
                end += 1
                ans = max(ans, zeros + ones)
                continue
            else:
                if zeros + 1 > k:
                    if snd_zero == -1:
                        snd_zero = end - 1
                        end += 1
                    while start < snd_zero:
                        tmp = nums[start]
                        if tmp:
                            ones -= 1
                        else:
                            zeros = max(0, zeros - 1)
                        start += 1

                    snd_zero = -1
                    tmp = nums[start]
                    if tmp:
                        ones -= 1
                    else:
                        zeros -= 1
                    start += 1
                    continue
                else:
                    zeros += 1
                    if snd_zero == -1: snd_zero = end
                    ans = max(ans, zeros + ones)
                    end += 1
                    continue

        return ans



# nums = [1,1,1,0,0,0,1,1,1,1,0]
# k = 2
# nums = [0,0,1,1,1,0,0]
# k = 0
nums = [
    1,0,0,1,0,
    0,1,0,1,1,
    1,1,0,1,1,
    1,1,0,1,1,
    1,1,1,1,0,
    1,1,1,0,0,
    1,1,1,0,0,
    1,0,1,0,0,
    1,0,0,1,1
]
k = 9
s = Solution()
ans = s.longestOnes(nums, k)
print(ans)
