class Solution:
    def reverseWords(self, s: str) -> str:
        words = list(filter(lambda w: len(w),s.strip().split(" ")))
        return " ".join(words[::-1])
