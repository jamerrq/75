from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # sorting by end point in ascending order
        points.sort(key=lambda x: x[1])
        # to store the current burst
        burst = points[0][1]
        # to keep track the number of bursts
        ans = 1
        # let's go greedy
        for i in range(1, len(points)):
            start_point = points[i][0]
            if start_point <= burst:
                continue

            ans += 1
            burst = points[i][1]

        return ans
