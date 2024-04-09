from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        c = {}
        def mark(start, group):
            if start in c:
                return

            c[start] = group
            neigs = [x for x in range(n) if isConnected[start][x]]
            for neig in neigs:
                mark(neig, group)

        ans = 0
        for i in range(n):
            #
            if i in c:
                continue
            else:
                mark(i, ans)
                ans += 1

        return ans
