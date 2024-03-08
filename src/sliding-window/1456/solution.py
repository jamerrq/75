class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        curr = sum([1 for c in s[:k] if c in "aeiou"])
        ans = curr
        for i in range(k, len(s)):
            curr += bool(s[i] in "aeiou")
            curr -= bool(s[i - k] in "aeiou")
            ans = max(ans, curr)
            if ans == k:
                break

        return ans
