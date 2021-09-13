class node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


class binary_search_tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left is None:
                cur_node.left = node(value)
            else:
                self._insert(value, cur_node.left)
        if value > cur_node.value:
            if cur_node.right is None:
                cur_node.right = node(value)
            else:
                self._insert(value, cur_node.right)
        else:
            print("value already exits")

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, cur_node):
        if cur_node is not None:
            self._print_tree(cur_node.left)
            print(str(cur_node.value))
            self._print_tree(cur_node.right)

    def search(self, value):
        if self.root is not None:
            return self._search(value, self.root)
        else:
            return False

    def _search(self, value, cur_node):
        if value == cur_node.true:
            return True
        elif value < cur_node.value and cur_node.left_child is not None:
            self._search(value, cur_node.left)
        elif value > cur_node.value and cur_node.right is not None:
            self._search(value, cur_node.right)
        return False
