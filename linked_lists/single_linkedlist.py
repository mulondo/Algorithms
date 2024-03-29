class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class linkedList:
    def __init__(self):
        self.head = Node()

    def addElement(self, data):
        new_node = Node(data)
        cur = self.head
        # cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = new_node

    def length(self):
        cur = self.head
        total = 0
        while cur.next is not None:
            total += 1
            cur = cur.next
        return total

    def display(self):
        elements = []
        cur = self.head

        while cur.next is not None:
            cur = cur.next
            elements.append(cur.data)
        print(elements)


linked_List = linkedList()

linked_List.addElement(1)
linked_List.addElement(2)
linked_List.addElement(5)
linked_List.addElement(6)
linked_List.addElement(8)
# linked_List.display()


# def addEl():
#     elem = [1, 3, 5, 6, 7, 9]
#     for e in elem:
#         linked_List.addElement(e)
#
#
# addEl()
linked_List.display()

# x = input("enter the element: ")
# print(x)
