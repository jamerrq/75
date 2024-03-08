from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = {}
        cols = [[] for _ in grid[0]]
        for row in grid:
            rowstr = "-".join(([str(x) for x in row]))
            rows[rowstr] = rows.get(rowstr, 0) + 1
            for i in range(len(row)):
                cols[i].append(row[i])

        print(rows)
        print(cols)
        ans = 0
        for i in range(len(cols)):
            coli = "-".join(([str(x) for x in cols[i]]))
            ans += rows.get(coli, 0)

        return ans
