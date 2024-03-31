from typing import List


class Solution:
    def __init__(self):
        self.mem = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        #
        if not n:
            return []
        #
        if n == 1:
            letters = self.mem[digits]
            return [x for x in letters]
        #
        first_letter = self.mem[digits[0]]
        digits = digits[1:]
        next_result = self.letterCombinations(digits)
        # letters = mem[first_letter]
        new_results = []
        for l in first_letter:
            for r in next_result:
                new_results.append(f'{l}{r}')

        return new_results

