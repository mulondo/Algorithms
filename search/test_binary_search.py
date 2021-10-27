class Node:
    def __init__(self, key=None):
        self.value = key
        self.left = None
        self.right = None


class binary_tree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._insert(val, self.root)

    def _insert(self, val, cur_node):
        new_node = Node(val)

        if val < cur_node.value:
            if cur_node.left is None:
                cur_node.left = new_node
            else:
                self._insert(val, cur_node.left)
        elif val > cur_node.value:
            if cur_node.right is None:
                cur_node.right = new_node
            else:
                self._insert(val, cur_node.right)
        else:
            print(" The value already exists")

    def display(self):
        if self.root is not None:
            self._display(self.root)

    def _display(self, cur_node):
        if cur_node is not None:
            self._display(cur_node.left)
            print(str(cur_node.value))
            self._display(cur_node.right)

    def search(self,val):
        if self.root is not None:
            return self._search(val,self.root)
        else:
            return False

    def _search(self, val, cur_node):
        if val == cur_node.value:
            print("This is the value :", cur_node.value)
        elif val < cur_node.value and cur_node.left is not None:
            return self._search(val,cur_node.left)
        elif val > cur_node.value and cur_node.right is not None:
            return self._search(val,cur_node.right)
        else:
            print ("The value does not exist")

by = binary_tree()
by.insert(9)
by.insert(4)
by.insert(1)
by.insert(6)
by.insert(7)
by.insert(8)
by.insert(10)
by.insert(5)
by.insert(12)
by.insert(2)
by.insert(3)
by.insert(0)
by.insert(0)

by.display()