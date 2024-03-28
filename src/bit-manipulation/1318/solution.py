class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ba, bb, bc = bin(a)[2:], bin(b)[2:], bin(c)[2:]
        ll = max(len(ba), len(bb), len(bc))
        ba, bb, bc = ba.zfill(ll), bb.zfill(ll), bc.zfill(ll)
        a = 0
        for i in range(ll):
            da = ba[i]
            db = bb[i]
            dc = bc[i]
            if dc == '0':
                a += int(da == '1')
                a += int(db == '1')
            else:
                if da != '1' and db != '1':
                    a += 1

        return a
