class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

    def insert(self,root, key):
        if root is None:
            return Node(key)
        else:
            if root.val == key:
                return root
            elif root.val < key:
                root.right = self.insert(root.right, key)
            else:
                root.left = self.insert(root.left, key)
        return root

     # A utility function to do inorder tree traversal
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.val)
            self.inorder(root.right)