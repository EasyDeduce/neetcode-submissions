class MyHashSet:

    def __init__(self):
        self.mset=set()

    def add(self, key: int) -> None:
        self.mset.add(key)

    def remove(self, key: int) -> None:
        if key not in self.mset:
            return
        self.mset.remove(key)

    def contains(self, key: int) -> bool:
        return (lambda x: True if x in self.mset else False)(key)


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)