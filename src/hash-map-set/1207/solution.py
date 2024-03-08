from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr.sort()
        mem = set()
        c = 0
        x = -1001
        for i in range(len(arr)):
            if arr[i] == x:
                c += 1
            else:
                if c in mem: return False
                if c: mem.add(c)
                c = 1
                x = arr[i]

        return not (c in mem)
