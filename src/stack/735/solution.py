from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        curr = []
        sign = None
        for i in range(len(asteroids)):
            ai = asteroids[i]
            si = bool(ai > 0)
            if not len(curr):
                curr = [ai]
                sign = si
                continue

            if si == sign:
                curr.append(ai)
                continue

            if si and not sign:
                curr.append(ai)
                sign = si
                continue

            include = True
            while len(curr):
                tmp = curr[-1]
                st = bool(tmp > 0)
                if -ai > tmp and st != si:
                    curr.pop()
                    continue
                if -ai == tmp:
                    include = False
                    curr.pop()
                    break

                if -ai < tmp and st != si:
                    include = False
                    break
                break

            if not len(curr) and include:
                curr = [ai]
                sign = si
                continue

            if include:
                curr.append(ai)
                sign = si
                continue

        return curr
