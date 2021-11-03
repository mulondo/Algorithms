class Node:
    def __init__(self, key=None):
        self.value = key
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root =  None

    def add_elements(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._add_element(value, self.root)

    def _add_element(self, value, current_node):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._add_element(value, current_node.left)
        elif value > current_node.value:
            if current_node.left is None:
                current_node.right = Node(value)
            else:
                self._add_element(value, current_node.right)
        else:
            print(f"The value {value} already exist")

    def display(self):
        if self.root is not None:
            self._display(self.root)

    def _display(self, current_node):
        if current_node is not None:
            print(current_node.value)
            self._display(current_node.left)
            self._display(current_node.right)

    def search

binary = BinaryTree()
binary.add_elements(6)
binary.add_elements(7)
binary.add_elements(1)
binary.add_elements(2)
binary.add_elements(14)
binary.add_elements(14)
binary.display()