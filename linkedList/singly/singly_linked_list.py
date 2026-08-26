class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


    
class LinkedList:
    def __init__(self):
        self.head = None
        
    def print_list(self):
        current = self.head

        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("None")   
        

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def swap_nodes(self, key_1, key_2):
        if key_1 == key_2:
            return
        prev_1 = None
        curr_1 = self.head

        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1
            curr_1 = curr_1.next
        
        prev_2 = None
        curr_2 = self.head
        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2
            curr_2 = curr_2.next
        
        if not curr_1 or not curr_2:
            return 
        
        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2
            
        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1
            
        curr_1.next, curr_2.next = curr_2.next, curr_1.next
            


# Testing
llist = LinkedList()

llist.append("A")
llist.append("B")
llist.append("C")

llist.swap_nodes("B", "C")

llist.print_list()
