'''
Find the middle of a given linked list in C
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def Find_middle(self):
        if not self.head:
            print("The List is Empty")
            return
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        print("The Middle Element is:", slow.data)

    def print_linkedlist(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Test the LinkedList
l = LinkedList()
l.append(1)
l.append(2)
l.append(3)
l.append(4)
l.append(5)

print("Linked List:")
l.print_linkedlist()

l.Find_middle()
