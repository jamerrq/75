class RecentCounter:

    def __init__(self):
        self.curr = []


    def ping(self, t: int) -> int:
        self.curr = [x for x in self.curr if x >= t - 3000]
        self.curr.append(t)
        return len(self.curr)



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
