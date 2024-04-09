class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        dp = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                ci = text1[i] if i < n else '-'
                cj = text2[j] if j < m else '-'
                if ci == cj:
                    pv = dp[i - 1][j - 1] if i and j else 0
                    dp[i][j] = pv + 1
                else:
                    pvi = dp[i - 1][j] if i else 0
                    pvj = dp[i][j - 1] if j else 0
                    dp[i][j] = max(pvi, pvj)

        return dp[-1][-1]
