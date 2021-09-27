class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        ha = 0
        for char in key:
            ha += ord(char)
        return ha % self.MAX

    def __setitem__(self, key, value):
        has_val = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[has_val]):
            if len(element) == 2 and element[0] == key:
                print('the index: ', idx, element)
                self.arr[has_val][idx] = (key, value)
                found = True
                break
        if not found:
            self.arr[has_val].append((key, value))

    def __getitem__(self, key):
        has_val = self.get_hash(key)
        return self.arr[has_val]
myhash = HashTable()
myhash['match 6'] = 85
myhash['match 6'] = 82
myhash['match 17'] = 20

print(myhash.arr)
