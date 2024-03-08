from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        c = 0
        m = 0
        for g in gain:
            c += g
            m = max(m, c)

        return m
