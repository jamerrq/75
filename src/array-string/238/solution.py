from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeros = 0
        for num in nums:
            if num != 0:
                product *= num
            else:
                zeros += 1
        new_array = []
        if zeros > 1:
            new_array = [0] * len(nums)
        elif zeros == 1:
            new_array = [0] * len(nums)
            for i in range(len(nums)):
                if nums[i] == 0:
                    new_array[i] = product
        else:
            for num in nums:
                if num != 0:
                    new_array.append(product // num)
                else:
                    new_array.append(product)
        return new_array
