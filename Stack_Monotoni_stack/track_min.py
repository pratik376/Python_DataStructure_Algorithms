from collections import deque

class min_stack:

    def __init__(self):
        self.stack=deque()
        self.aux_stack=deque()
        self.min_element=float('inf')

    def push(self,element):
        self.stack.append(element)

        if (element<= self.min_element):
            self.min_element=element
            self.aux_stack.append(self.min_element)

        # self.min_element=min(self.min_element,element)
        # self.aux_stack.append(self.min_element)    

    def pop(self):

        element=self.stack.pop()
        

        if self.aux_stack[-1]==element:
            self.aux_stack.pop()

        self.min_element=self.aux_stack[-1]    

        return element    

    def getMin(self):

        return self.aux_stack[-1]
    
    def top_element(self):

        return self.stack[-1]
    


s=min_stack()

s.push(1)
s.push(2)
s.push(0)
print(s.pop())
print(s.getMin())
print(s.top_element())
print(s.pop())
print(s.getMin())
            