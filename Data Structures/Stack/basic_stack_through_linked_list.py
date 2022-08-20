class Element:
    def __init__(self,value):
        self.value = value
        self.next = None
        
class Stack:
    def __init__(self):
        self.base = None
        self.previous_mins = list()
        self.previous_maxs = list()
        self.min = float("inf")
        self.max = 0
        
    def push(self,value):
        if value <= self.min:
            self.previous_mins.append(self.min)
            self.min = value
            
        if value > self.max:
            self.previous_maxs.append(self.max)
            self.max = value
        
        if self.base is None:
            self.base = Element(value)
        else:
            new_element = Element(value)
            new_element.next = self.base
            self.base = new_element
        
        
    def print_stack(self,base):
        if base is None:
            return
        else:
            print(base.value)
            self.print_stack(base.next)
    
    def pop(self):
        if self.base is None:
            print("Empty Stack ...!")
        else:
            top_element = self.base
            self.base = self.base.next
            top_element.next = None
            if self.min == top_element.value:
                self.min = self.previous_mins.pop()
            if self.max == top_element.value:
                self.max = self.previous_maxs.pop()
            return top_element
        
    def min_element_of_stack(self):
        # to be implemented
        return self.min
    
    def max_element_of_stack(self):
        # to be implemented
        return self.max
        
        
if __name__ == "__main__":
    stack = Stack()
    
    stack.push(4)
    stack.push(5)
    stack.push(6)
    stack.push(1)
    stack.push(10)
    stack.push(100)
    stack.push(0)
    base = stack.base
    stack.print_stack(base)
    element = stack.pop()
    print("Element: " + str(element.value) + " poped from stack")
    base = stack.base
    stack.print_stack(base)
    print("The maximum element in stack is: " + str(stack.max_element_of_stack()))
    print("The minimum element in stack is: " + str(stack.min_element_of_stack()))
    element = stack.pop()
    print("Element: " + str(element.value) + " poped from stack")
    base = stack.base
    stack.print_stack(base)
    print("The maximum element in stack is: " + str(stack.max_element_of_stack()))
    print("The minimum element in stack is: " + str(stack.min_element_of_stack()))
    element = stack.pop()
    element = stack.pop()
    print("Element: " + str(element.value) + " poped from stack")
    base = stack.base
    stack.print_stack(base)
    print("The maximum element in stack is: " + str(stack.max_element_of_stack()))
    print("The minimum element in stack is: " + str(stack.min_element_of_stack()))
    