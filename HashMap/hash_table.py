class Node:
    def __inti__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __inti__(self):
        self.capacity = 90
        self.size = 0
        self.buckets = [None] * self.capacity

    def hash(self, key):
        hashsum = 0
        for idx, c in enumerate(key):
            hashsum += (idx + len(key))