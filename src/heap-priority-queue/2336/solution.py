class SmallestInfiniteSet:

    def __init__(self):
        self.excluded = set()
        self.smallest = 1

    def popSmallest(self) -> int:
        sm = 1
        while sm in self.excluded:
            sm += 1
        self.excluded.add(sm)
        return sm

    def addBack(self, num: int) -> None:
        if num in self.excluded:
            self.excluded.remove(num)



# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
