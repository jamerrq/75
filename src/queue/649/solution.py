class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        L = list(senate)
        #
        ds = 0
        rs = 0
        #
        for x in L:
            if x == 'D': ds += 1
            else: rs += 1
        #
        while ds and rs:
            curr = L.pop(0)
            for i in range(len(L)):
                tmp = L[i]
                if tmp != curr:
                    L.pop(i)
                    if tmp == 'D':
                        ds -= 1
                    else:
                        rs -= 1
                    break
            L.append(curr)
        #
        return 'Radiant' if L[0] == 'R' else 'Dire'
