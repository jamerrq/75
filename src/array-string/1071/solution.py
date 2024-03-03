class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        prefix = ""
        index = 0
        l1 = len(str1); l2 = len(str2)
        longest = ""
        while index < min(l1, l2):
            if str1[index] == str2[index]:
                prefix += str1[index]
                index += 1
            else:
                return ""
            #
            m1 = l1 // index
            m2 = l2 // index
            #
            if prefix * m1 == str1 and prefix * m2 == str2:
                longest = prefix

        return longest


# Another approach
"""
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        return str1[0:math.gcd(len(str1), len(str2))]
"""
