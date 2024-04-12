class StockSpanner:

    def __init__(self):
        self.stack = []
        self.n = 0

    def next(self, price: int) -> int:
        if not self.n or self.stack[-1][0] > price:
            self.stack.append((price, 1))
            self.n += 1
            return 1

        temp = 0
        while self.n and self.stack[-1][0] <= price:
            curr = self.stack.pop()
            temp += curr[1]
            self.n -= 1

        self.stack.append((price, temp + 1))
        self.n += 1
        return temp + 1


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
