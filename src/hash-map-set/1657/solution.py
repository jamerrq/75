class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        w1 = "".join(sorted([x for x in word1]))
        w2 = "".join(sorted([x for x in word2]))

        if w1 == w2: return True

        if len(w1) != len(w2): return False

        s1, s2 = set(w1), set(w2)
        if s1 != s2: return False
        l1 = sorted([w1.count(s) for s in s1])
        l2 = sorted([w2.count(s) for s in s2])

        return l1 == l2
