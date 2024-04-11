from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) \
        -> List[int]:
        #
        potions.sort()
        n = len(spells)
        y = len(potions)
        #
        ans = [0] * n
        #
        m = {}
        k = 0
        for spell in spells:
            #
            if spell in m:
                ans[k] = m[spell]
                k += 1
                continue

            # binary search
            i = 0
            j = y - 1
            # we are looking for the min index
            # i on potions such that
            # spell * potions[i] >= sucess
            mid = 0
            x = 0
            while i < j:
                mid = (i + j) // 2
                pot = potions[mid]
                #
                x = pot * spell
                #
                if x >= success:
                    j = mid
                    continue
                if x < success:
                    i = mid + 1
                    continue

            ans[k] = y - i if potions[i] * spell >= success else 0
            m[spell] = ans[k]
            k += 1
            continue

        return ans
