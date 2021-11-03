class Node:
    def __init__(self, key):
        self.data = key
        self.next = None

class LinkList:
    def __init__(self):
        self.head = Node()

    def add_element(self, value):
        current_node = self.head
        new_node = Node(value)
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

