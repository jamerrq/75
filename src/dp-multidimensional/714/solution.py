from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [0, 0]
        tmp = [0, 0]
        for i in range(n - 1, -1, -1):
            for j in [1, 0]:
                if j:
                    tmp[j] = max(-prices[i] + dp[0], dp[1])
                else:
                    tmp[j] = max(prices[i] - fee + dp[1], dp[0])

            dp = tmp

        return dp[1]
