class Node:
    def __init__(self, data = None, left = None, right = None):
        self.value = data
        self.left = None
        self.right = None

class  BinaryTree:
    def __init__(self):
        self.root = None

    def insert_data(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._insert_data(val, self.root)

    def _insert_data(self, value, cur_node):
        new_node = Node(value)
        if value < cur_node.value:
            if cur_node.left is None:
                cur_node.left = new_node
            else:
                self._insert_data(value, cur_node.left)
        if value > cur_node.value:
            if cur_node.right is None:
                cur_node.right = new_node
            else:
                self._insert_data(value, cur_node.right)
        if value == cur_node.value:
            print(f"This {value} already exits")

    def display(self):
        if self.root is not None:
            return self._display(self.root)

    def _display(self, cur_node):
        if cur_node!= None:
            self._display(cur_node.left)
            print(str(cur_node.value))
            self._display(cur_node.right)

# b = BinaryTree()
# b.insert_data(6)
# b.insert_data(4)
# b.insert_data(4)
# b.insert_data(12)
# b.insert_data(5)
# b.insert_data(8)
# b.insert_data(2)

# b.display()
