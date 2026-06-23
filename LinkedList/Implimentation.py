class Node:

    def __init__(self,value):

       self.value= value
       self.next=None

class LinkedList:

    def __init__(self):
        self.head=None

    def append(self, value):

        new_node=Node(value)

        if self.head is None:
            self.head= new_node
            return
        
        current= self.head

        while current.next :
            current=current.next

        current.next= new_node

    def display(self):

        current= self.head

        while current :
            print(current.value)
            current= current.next

    def prepand(self, value):

        new_node= Node(value)

        new_node.next=self.head

        self.head=new_node

    def delete(self, value):

        if not self.head:
            return

        if self.head.value== value:
            self.head=self.head.next

        current= self.head

        while current.next and current.next.value != value:
            current=current.next

        if current.next:
            current.next= current.next.next
                                

                        
        

a=Node(10)
b=Node(20)
c=Node(30)

a.next=b
b.next=c
