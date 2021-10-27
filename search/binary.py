# class Node:
#     def __init__(self, key=None):
#         self.left = None
#         self.right = None
#         self.value = key
#
#
# class BinaryTree:
#
#     def __init__(self):
#         self.root = None
#
#     def insert(self, value):
#
#         if self.root is None:
#             self.root = Node(value)
#         else:
#             self._insert(value, self.root)
#
#     def _insert(self, value, current_node):
#         print('----------> :', value)
#         if value < current_node.value:
#             if current_node.left is None:
#                 current_node.left = Node(value)
#             else:
#                 self._insert(value, current_node.left)
#
#         elif value > current_node.value:
#             if current_node.right is None:
#                 current_node.right = Node(value)
#             else:
#                 self._insert(value, current_node.right)
#         else:
#             print(f'The value {value} already exists')
#
#     def display(self):
#         if self.root is not None:
#             self._display(self.root)
#
#     def _display(self, current_node):
#         if current_node is not None:
#             self._display(current_node.left)
#             print(str(current_node.value))
#             self._display(current_node.right)
#
#     def search(self, value):
#         if self.root is not None:
#             self._search(self.root, value)
#
#     def _search(self, current_node, value):
#         if value == current_node.value:
#             print(f"The value {current_node.value} is found")
#
#         elif value < current_node.value and current_node.left is not None:
#             self._search(current_node.left, value)
#         elif value > current_node.value and current_node.right is not None:
#             self._search(current_node.right, value)
#         else:
#             print(f"the element {value} is not found")
#
#
# by = BinaryTree()
# by.insert(12)
# by.insert(1)
# by.insert(10)
# by.insert(2)
# by.insert(4)
# by.display()
#
# by.search(96)

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


class BinaryTree:

    def __init__(self):
        self.root = None

    def add_elements(self, element):

        if self.root is None:
            self.root = Node(element)
        else:
            self._add_elements(element, self.root)

    def _add_elements(self, element, current_node):

        if element < current_node.value:
            if current_node.left is None:
                current_node.left = Node(element)
            else:
                self._add_elements(element, current_node.left)
        elif element > current_node.value:
            if current_node.right is None:
                current_node.right = Node(element)
            else:
                self._add_elements(element, current_node.right)
        else:
            print(f"The element {element} already exists")

    def display(self):
        if self.root is not None:
            self._display(self.root)

    def _display(self, current_node):
        if current_node:
            self._display(current_node.left)
            if current_node.value is not None:
                print(current_node.value)
            self._display(current_node.right)

    def search(self, element):

        if self.root is not None:
            self._search(self.root, element)

    def _search(self, current_node, element):
        if current_node.value == element:
            print(f"The element {current_node.value} is found")

        elif element < current_node.value and current_node.left is not None:
            self._search(current_node.left, element)

        elif element > current_node.value and current_node.right is not None:
            self._search(current_node.right, element)
        else:
            print(f"The element {element} does not exist")

    def delete(self, element):

        if self.root is not None:
            self._delete(self.root, element)

    def _delete(self, current_node, element):
        if current_node.value == element:
            current_node.value = None

        elif element < current_node.value and current_node.left is not None:
            self._delete(current_node.left, element)

        elif element > current_node.value and current_node.right is not None:
            self._delete(current_node.right, element)
        else:
            print(f"The element {element} does not exist")




mybin = BinaryTree()
mybin.add_elements(5)
mybin.add_elements(12)
mybin.add_elements(9)
mybin.add_elements(1)
mybin.add_elements(8)
# mybin.add_elements(5)
print("this is the display before delete")
mybin.display()

print("---------------------------")

# mybin.search(5)
mybin.delete(5)
print("this is the display before after delete")
mybin.display()
