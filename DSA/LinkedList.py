print("This is a Linked List implementation in Python")
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
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")
    def delete(self, key):
        current_node = self.head
        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return
        prev_node = None
        while current_node and current_node.data != key:
            prev_node = current_node
            current_node = current_node.next
        if not current_node:
            return
        prev_node.next = current_node.next
        current_node = None
    def search(self, key):
        current_node = self.head
        while current_node:
            if current_node.data == key:
                return True
            current_node = current_node.next
        return False
    def insert_after(self, prev_node_data, data):
        current_node = self.head
        while current_node and current_node.data != prev_node_data:
            current_node = current_node.next
        if not current_node:
            return
        new_node = Node(data)
        new_node.next = current_node.next
        current_node.next = new_node
    def reverse(self):
        prev_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node
    def length(self):
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count
    def get_middle(self):
        slow = self.head
        fast = self.head
        if not self.head:
            return None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data if slow else None
    def remove_duplicates(self):
        current_node = self.head
        seen = set()
        prev_node = None
        while current_node:
            if current_node.data in seen:
                prev_node.next = current_node.next
            else:
                seen.add(current_node.data)
                prev_node = current_node
            current_node = current_node.next

print("Linked List operations:")
llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(2)
llist.append(4)         
llist.display()  # Output: 1 -> 2 -> 3 -> 2 -> 4 -> None
llist.delete(2)
llist.display()  # Output: 1 -> 3 -> 2 -> 4 -> None     
llist.insert_after(3, 5)
llist.display()  # Output: 1 -> 3 -> 5 -> 2 -> 4 -> None
print("Search for 3:", llist.search(3))  # Output: True
print("Search for 6:", llist.search(6))  # Output: False
llist.reverse()
llist.display()  # Output: 4 -> 2 -> 5 -> 3 -> 1 -> None
print("Length of Linked List:", llist.length())  # Output: 5
print("Middle element:", llist.get_middle())  # Output: 5
llist.remove_duplicates()
llist.display()  # Output: 1 -> 3 -> 5 -> 2 -> 4 -> None
print("Reversing the Linked List:")
llist.reverse()
llist.display()  # Output: 4 -> 2 -> 5 -> 3 -> 1 -> None
print("Linked List implementation complete.")
# This code implements a basic Linked List in Python with various operations such as append, delete, search, insert after, reverse, length, get middle element, and remove duplicates.
# The LinkedList class provides methods to manipulate the linked list, and the Node class represents each node in the list.
# The code includes examples of how to use the LinkedList class and its methods.