class Node:
    def __init__(self, key=None):
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

    def length(self):
        current_node = self.head
        total = 0
        while current_node.next is not None:
            total += 1
            current_node = current_node.next
        return total

    def display(self):
        current_node = self.head
        elements = []
        while current_node.next is not None:
            current_node = current_node.next
            elements.append(current_node.data)
        return elements


linked_list = LinkList()
linked_list.add_element(7)
linked_list.add_element(2)
linked_list.add_element(5)
linked_list.add_element(8)
linked_list.add_element(10)
linked_list.add_element(1)
print(linked_list.length())
print(linked_list.display())
