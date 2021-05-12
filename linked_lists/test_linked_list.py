class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = Node()

    def insert(self,val):
        new_node = Node(val)
        cur_node = self.head
        while cur_node.next!=None:
            cur_node = cur_node.next
        cur_node.next = new_node