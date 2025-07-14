'''
Find the middle of a given linked list in C
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self,data):
        self.head = None

    # Function to append a new node at the end of the list
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # Function to find the middle of the linked list
    def find_middle(self):
        if not self.head:
            print("The list is empty.")
            return

        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next          # Move slow by one step
            fast = fast.next.next     # Move fast by two steps

        print("The middle element is:", slow.data)

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)

print("Linked List:")
ll.print_list()


ll.find_middle()
