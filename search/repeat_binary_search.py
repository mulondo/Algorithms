class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


class BinarySearch:

    def __init__(self):
        self.root = None

    def add_elements(self, element):
        if self.root is None:
            self.root = Node(element)
        else:
            self._add_element(element, self.root)

    def _add_element(self, element, current_node):

        if element < current_node.value:
            if current_node.left is None:
                current_node.left = Node(element)
            else:
                self._add_element(element, current_node.left)
        elif element > current_node.value:
            if current_node.right is None:
                current_node.right = Node(element)
            else:
                self._add_element(element, current_node.right)
        else:
            print(f"the element {element} already exists")

bi = BinarySearch()
bi.add_elements(10)
bi.add_elements(2)
bi.add_elements(4)
bi.add_elements(8)
bi.add_elements(1)
bi.add_elements(9)
bi.add_elements(2)
bi.add_elements(10)