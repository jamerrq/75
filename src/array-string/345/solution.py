class Solution:
    def reverseVowels(self, s: str) -> str:
        vows = [x for x in s if x in "aeiouAEIOU"]
        return "".join([x if x not in "aeiouAEIOU" else vows.pop() for x in s])
