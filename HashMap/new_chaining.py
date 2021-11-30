class HashTable:
    """
        Hash table class
    """
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        """
        this function generates a hash
        """
        ha = 0
        for char in key:
            ha += ord(char)
        return ha % self.MAX

    def __setitem__(self, key, value):
        """
        :param key:
        :param value:
        :return:
        """
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
        """
        :param key:
        :return:
        """
        has_val = self.get_hash(key)
        for idx, element in enumerate(self.arr[has_val]):
            if len(element) < 2:
                print('Value not found')
            elif element[0] == key:
                return element[1]


my_hash = HashTable()
my_hash['match 6'] = 85
my_hash['match 6'] = 82
my_hash['match 20'] = 45
my_hash['match 12'] = 100
my_hash['match 17'] = 20

print('this is the result: ', my_hash['match 6'])
