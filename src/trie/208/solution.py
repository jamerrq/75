class Trie:

    def __init__(self):
        self.mem = set([])
        self.pre = set([])

    def insert(self, word: str) -> None:
        #
        for i in range(len(word)):
            self.pre.add(word[:i + 1])

        self.mem.add(word)

    def search(self, word: str) -> bool:
        return word in self.mem

    def startsWith(self, prefix: str) -> bool:
        return prefix in self.pre


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
