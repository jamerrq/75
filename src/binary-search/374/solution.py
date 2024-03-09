# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    if num: pass

class Solution:
    def guessNumber(self, n: int) -> int:
        init = (n + 1) // 2
        lower = 1
        higher = n
        g = guess(init)
        while g:
            if g > 0:
                lower = init + 1
            else:
                higher = init
            init = (higher + lower) // 2
            g = guess(init)

        return init
