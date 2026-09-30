class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_elem(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = Node(data)

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_any_pos(self, position, data):
        if position < 0 or position > self.length():
            return "Invalid Postion"
        if position == 0:
            self.insert_at_start(data)
            return
        new_node = Node(data)
        curr = self.head
        for _ in range(position - 1):
            curr = curr.next
        new_node.next = curr.next
        curr.next = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head  # at first we assign to head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def del_from_beginning(self):
        if self.head is None:
            return None
        self.head = self.head.next

    def length(self):
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        return count

    def del_from_any_pos(self, position):
        if position < 0 or position >= self.length():
            return "Invalid postion"

        if position == 0:
            self.del_from_beginning()
            return

        curr = self.head

        for _ in range(position - 1):
            curr = curr.next
        curr.next = curr.next.next

    def search(self, data):
        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                return True
            current_node = current_node.next
        return False

    def display(self):
        elements = []
        curr_node = self.head
        while curr_node:
            elements.append(curr_node.data)
            curr_node = curr_node.next
        print(elements)

    def reverse(self, head):
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev

    def sort(self, head):
        if not self.head:
            return
        swapped = True
        while swapped:
            swapped = False
            curr = self.head
            while curr.next:
                if curr.data > curr.next.data:
                    curr.data, curr.next.data = curr.next.data, curr.data
                    swapped = True
                curr = curr.next
    
linked_list = LinkedList()
linked_list.add_elem(4)
linked_list.add_elem(2)
linked_list.add_elem(1)
linked_list.add_elem(3)
# linked_list.insert_at_start()
# linked_list.insert_at_any_pos(2, "Z")
# linked_list.insert_at_end("-")
# linked_list.del_from_beginning()
# print(linked_list.search("B"))
print(linked_list.length())
# linked_list.del_from_any_pos(1)
# linked_list.reverse(linked_list.head)
linked_list.sort(linked_list.head)
linked_list.display()
