class Node:
    
    def __init__(self,value):
        self.val = value
        self.next = None
        
class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def insert_at_last(self,value):
        # intialize new node
        new_node = Node(value)
        
        # setting the new node to the head
        if self.head == None:
            self.head = new_node
            
        # set the new node to the last of the list by traversing list upto the end
        else:
            temp_node = self.head
            while(temp_node.next != None):
                temp_node = temp_node.next
            temp_node.next = new_node
            
    def insert_at_top(self,value):
        # initialize new node
        new_node = Node(value)
        
        # setting new node to the head
        if self.head is None:
            self.head = new_node
            
        # assign head to the next of new node and call new node the head of the list
        else:
            new_node.next = self.head
            self.head = new_node
            
    def traverse(self):
        temp_node = self.head
        if temp_node != None:
            while(temp_node != None):
                print(temp_node.val)
                temp_node = temp_node.next
        else:
            print("Empty list ...!")
            
    def find_middle_of_list(self):
        temp_node = self.head
        slow_pointer = temp_node
        fast_pointer = temp_node
        
        while fast_pointer is not None and fast_pointer.next is not None:
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next
        print("The middle of the list: " + str(slow_pointer.val))
        
    def reverse_the_list(self):
        temp_node = self.head
        
        current = temp_node.next
        temp_current = temp_node.next
        previous = temp_node
        
        while current.next is not None:
            current = current.next
            temp_current.next = previous
            previous = temp_current
            temp_current = current
            
        self.head.next = None
        current.next = previous
        self.head = current
    
list = LinkedList()
list.insert_at_last(4)
list.insert_at_last(5)
list.insert_at_last(6)
list.insert_at_last(7)
list.insert_at_top(2)
list.insert_at_top(1)
list.insert_at_last(8)
list.insert_at_last(9)
list.insert_at_last(10)
list.traverse()
list.find_middle_of_list()
print("After reversing the linkedlist")
list.reverse_the_list()
list.traverse()
print("Insert 0 at last and 11 at top of the list")
list.insert_at_last(0)
list.insert_at_top(11)
list.traverse()
print("After reversing the linkedlist")
list.reverse_the_list()
list.traverse()
list.find_middle_of_list()