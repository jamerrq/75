from typing import List


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        ans = []
        tmp = ""
        for char in searchWord:
            tmp += char
            products = sorted(filter(lambda x: x.startswith(tmp), products))
            ans.append([x for x in products][:3])

        return ans
