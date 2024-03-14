from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def aux(index, mem = set(), vs=[]):
            if vs[index]:
                return

            vs[index] = True
            for x in rooms[index]:
                mem.add(x)
                aux(x, mem, vs)

        mem = set()
        vs = [False] * len(rooms)
        aux(0, mem, vs)
        return len([x for x in mem if x]) == len(rooms) - 1
