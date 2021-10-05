class HashTable:
    """
    Defines the behavior of a hashmap
    """
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX

    def __setitem__(self, key, value):
        """
        :param key:
        :param value:
        :return:
        """
        h = self.get_hash(key)
        self.arr[h] = value

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]


myhash = HashTable()
myhash['march 6'] = 150
myhash['march 17'] =120

print('This is the value :', myhash['march 6'])
