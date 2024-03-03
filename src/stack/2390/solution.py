class Solution:
    def removeStars(self, s: str) -> str:
        tmp = 0
        ans = ""
        for c in s:
            if c == '*':
                tmp += 1
                continue

            if tmp:
                ans = ans[:-tmp]
                tmp = 0

            ans += c

        if tmp:
            ans = ans[:-tmp]

        return ans
