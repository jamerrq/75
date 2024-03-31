import heapq
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        #
        wait = [(temperatures[0], 0)]
        heapq.heapify(wait)

        _ans = [0] * n
        for i in range(1, len(temperatures)):
            ti = temperatures[i]
            while len(wait) and wait[0][0] < ti:
                _, j = heapq.heappop(wait)
                _ans[j] = i - j
            #
            heapq.heappush(wait, (ti, i))

        return _ans
