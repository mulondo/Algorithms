class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = Node()

    def addElement(self,data):
        new_node = Node(data)
        cur = self.head
        while cur.next!=None:
            cur = cur.next
        cur.next = new_node

    def length(self):
        cur = self.head
        total = 0
        while cur.next!=None:
            total +=1
            cur = cur.next
        return total

    def display(self):
        elements = []
        cur = self.head

        while cur.next!=None:
            cur = cur.next
            elements.append(cur.data)
        print(elements)

linkedList = linked_list()
def addEl():
    elem = [1,3,5,6,7,9]
    for e in elem:
        linkedList.addElement(e)
addEl()
linkedList.display()

x = input("enter the element: ")
print(x)
