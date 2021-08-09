
class HashTable:

    def __init__(self):
        self.max = 10
        self.arr = [None for i in range(self.max)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.max

    def add(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val

    def get(self, key):
        h = self.get_hash(key)
        return self.arr[h]
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val
    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]
    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None


t = HashTable()
# t.add('name', 'moses')
# t['name'] = 'moses'
# print(t['name'])
print(t.get_hash('march 6'))
# print(t.get_hash('march 17'))