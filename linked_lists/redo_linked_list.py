# class Node:
#     def __init__(self, value= None):
#         self.data = value
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = Node()

#     def insert_element(self, element):
#         new_node = Node(element)
#         cur_node = self.head
#         while cur_node.next is not None:
#             cur_node = cur_node.next
#         cur_node = new_node
    # def insert_element(self, element):
    #     new_node = Node(element)
    #     cur_node = self.head
    #     while cur_node.next is not None:
    #         cur_node = cur_node.next
    #     cur_node = new_node

class Node:
    def __init__(self, value=None):
        self.data = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()

    def insert(self, element):
        new_node = Node()
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
        cur_node = new_node