

class Node:
    def __init__(self, data=None, nxt=None):
        self.data = data
        self.next = nxt
    
    def __str__(self):
        return str(self.data)


    def print_list(node):
        while node:
            print(node)
            node = node.next

    def return_last(node):
        while node:
            node = node.next
        return node.next

    def remove_second(list):
        if list == None:
            return None
        first = list
        second = list.next
        first.next = second.next
        second.next = None
        return second

class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None
    
    def add_first(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        self.length += 1
        return print_list(node)

    def add_end(self,data):
        node = Node(data)
        ptr = return_last(node)
        ptr.next = node.next
        return print_list(node)







node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.next = node3

