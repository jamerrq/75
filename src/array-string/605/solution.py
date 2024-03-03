from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        index = 0
        lf = len(flowerbed)
        while index < lf and n:
            if flowerbed[index]:
                index += 1
                continue
            left = index == 0 or not flowerbed[index - 1]
            right = index == lf - 1 or not flowerbed[index + 1]
            if left and right:
                n -= 1
                flowerbed[index] = 1
                index +=1
            index += 1

        return not n
