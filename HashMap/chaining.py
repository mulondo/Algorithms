class HashTable:
    """
    Hash table class
    """
    def __init__(self):
        self.max = 10
        self.arr = [[] for i in range(self.max)]

    def get_hash(self, key):
        """
        :param key:
        :return:
        """
        hn = 0
        for char in key:
            hn += ord(char)
        val = hn % self.max
        return val

    def __setitem__(self, key, val):
        hf = self.get_hash(key)
        found = False
        for index, element in enumerate(self.arr):
            # self.arr[hf].append((key, val))
            if len(element) == 2 and element[0] == key:
                self.arr[hf][index] = (key, val)
                found = True
                break

        if not found:
            self.arr[hf].append((key, val))

    def __getitem__(self, key):
        hf = self.get_hash(key)
        return self.arr[hf]


h = HashTable()
h["march 6"] = 120
h["march 8"] = 124
h["march 24"] = 85

# print(h["march 17"])

print("\n", h["march 6"])



# class Hashmap:

#     def __init__(self):
#         self.max = 10
#         self.arr = [[] for i in range(self.max)]

#     def get_hash(self, key):
#         h = 0
#         for char in key:
#             h += ord(char)
#         return h % self.max

#     def __setitem__(self, key, val):
#         h = self.get_hash(key)
#         found = False
#         for index, element in enumerate(self.arr):
#             if len(element) ==2 and element[0]==key:
#                 self.arr[h][index] = [key, val]
#                 found = True
#                 break
#         if not found:
#             self.arr[h] = [key, val]

#     def __getitem__(self, key):
#         hf = self.get_hash(key)
#         return self.arr[hf]

# hm = Hashmap()
# hm["march 6"] = 120
# hm["march 6"] = 124
# hm["march 24"] = 85

# # print(h["march 17"])

# print("\n", hm["march 6"])