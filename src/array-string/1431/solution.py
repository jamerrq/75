from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        return list(map(lambda x: x + extraCandies >= maxCandies, candies))
