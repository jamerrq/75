from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        curr = chars[0]
        cont = 0
        for _ in range(len(chars)):
            tmp = chars.pop(0)
            if tmp == curr:
                cont += 1
                continue
            else:
                chars.append(curr)
                curr = tmp
                if cont == 1:
                    continue
                scont = str(cont)
                for c in scont: chars.append(c)
                cont = 1

        chars.append(curr)
        if cont > 1:
            scont = str(cont)
            for c in scont: chars.append(c)

        return len(chars)
