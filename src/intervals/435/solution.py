from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prev = intervals[0]
        ans = 0
        for i in range(1, len(intervals)):
            iv = intervals[i]
            if iv[0] >= prev[1]:
                prev = iv
                continue
            if iv[0] >= prev[0] and iv[1] <= prev[1]:
                prev = iv
                ans += 1
                continue

            # last case
            ans += 1
            continue

        return ans
