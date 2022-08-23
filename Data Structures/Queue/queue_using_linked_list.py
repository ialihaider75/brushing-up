class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
      
    def is_empty(self):
        if self.front is None:
            return True
        else:
            return False

    def enqueue(self,value):
        if self.is_empty():
            node = Node(value)
            self.front = node
            self.rear = node
        else:
            new_node = Node(value)
            self.rear.next = new_node
            self.rear = new_node
            
    def dequeue(self):
        if not self.is_empty():
            element = self.front
            self.front = self.front.next
            element.next = None
            return element
    
    def print_queue(self,front):
        if front is not None:
            print(front.value)
            self.print_queue(front.next)
    
queue = Queue()
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)
queue.enqueue(7)
front = queue.front
print("Intital queue")
queue.print_queue(front)
element = queue.dequeue()
print("The element: " + str(element.value) + " is dequeued")
print("Queue after dequeue")
front = queue.front
queue.print_queue(front)