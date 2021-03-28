class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class binary_search_tree:
    def __init__(self):
        self.root = None
    def insert(self,value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert(value,self.root)

    def _insert(self,value,current_node):
        if value < current_node.value:
            if current_node.left == None:
                current_node.left = Node(value)
            else:
                self._insert(value,current_node.left)
        elif value > current_node.value:
            if current_node.right == None:
                current_node.right = Node(value)
            else:
                self._insert(value,current_node.right)
        else:
            print("This value already exist")