class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        # Add a new node at the end of the list
        if self.head is None:
            self.head = Node(data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(data)

    def prepend(self, data):
        # Add a new node at the beginning of the list
        new = Node(data)
        new.next = self.head
        self.head = new

    def insert(self, index, data):
        if index < 0:
            return False
        if index == 0:
            self.prepend(data)
            return True
        curr = self.head
        idx = 0
        while curr and idx < index - 1:
            curr = curr.next
            idx += 1
        if curr is None:
            return False
        new = Node(data)
        new.next = curr.next
        curr.next = new
        return True

    def remove(self, data):
        if self.head is None:
            return False
        if self.head.data == data:
            self.head = self.head.next
            return True
        curr = self.head
        while curr.next:
            if curr.next.data == data:
                curr.next = curr.next.next
                return True
            curr = curr.next
        return False

    def remove_at(self, index):
        if index < 0 or self.head is None:
            return False
        if index == 0:
            self.head = self.head.next
            return True
        idx = 0
        curr = self.head
        while curr.next and idx < index - 1:
            curr = curr.next
            idx += 1
        if curr.next is None:
            return False
        curr.next = curr.next.next
        return True

    def search(self, data):
        # Find whether a node containing the given data exists
        curr = self.head
        while curr:
            if curr.data == data:
                return True
            curr = curr.next
        return False

    def get(self, index):
        if index < 0:
            return None
        idx = 0
        curr = self.head
        while curr and idx < index:
            curr = curr.next
            idx += 1
        return curr.data if curr else None

    def size(self):
        # Return the number of nodes in the list
        curr = self.head
        cnt = 0
        while curr:
            curr = curr.next
            cnt += 1
        return cnt

    def is_empty(self):
        # Return whether the linked list contains no nodes
        return self.head is None

    def reverse(self):
        # Reverse the order of the nodes in the list
        prev = None
        curr = self.head
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        self.head = prev

    def display(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print()