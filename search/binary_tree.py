class Node:
    def __init__(self, key=None):
        self.left = None
        self.right = None
        self.value = key


class BinaryTree:
    def __init__(self):
        self.root = None

    def add_element(self, value):

        if self.root is None:
            self.root = Node(value)
        else:
            self._add_element(self.root, value)

    def _add_element(self, current_node, value):
        print(f"this is the element{value} --------> {current_node.value}")
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._add_element(current_node.left, value)

        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._add_element(current_node.right, value)
        else:
            print(f"This {value} already exists")

    def display(self):
        if self.root is not None:
            self._display(self.root)

    def _display(self, current_node):
        if current_node is not None:
            self._display(current_node.left)
            if current_node.value is not None:
                print(current_node.value)
            self._display(current_node.right)

    def search(self, value):
        if self.root is not None:
            self._search(self.root, value)

    def _search(self, current_node, value):
        if current_node.value == value:
            print(f"The element {value} is found")
        elif value < current_node.value and current_node.left is not None:
            self._search(current_node.left, value)
        elif value > current_node.value and current_node.right is not None:
            self._search(current_node.right, value)
        else:
            print(f"This {value} doesnot exist")

    def delete(self, value):
        if self.root is not None:
            self._delete(self.root, value)

    def _delete(self, current_node, value):
        if current_node.value == value:
            current_node.value = None
        elif value < current_node.value and current_node.left is not None:
            self._delete(current_node.left, value)
        elif value > current_node.value and current_node.right is not None:
            self._delete(current_node.right, value)
        else:
            print(f"This {value} doesnot exist")


bina = BinaryTree()
bina.add_element(6)
bina.add_element(4)
bina.add_element(10)
bina.add_element(12)
bina.add_element(3)
bina.add_element(1)
bina.add_element(1)
bina.add_element(5)
# bina.display()
# bina.search(20)
# bina.delete(10)
bina.display()




