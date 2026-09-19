class HashTable:
    def __init__(self, capacity):
        self.bucketSize = capacity
        self.hashTable = [[] for _ in range(capacity)]

    def _hash(self, key):
        return key % self.bucketSize

    def put(self, key):
        index = self._hash(key)
        self.hashTable[index].append(key)

    def remove(self, key):
        index = self._hash(key)
        if key in self.hashTable[index]:
            self.hashTable[index].remove(key)