class ListNode:

    def __init__(self, val=0, next=None):

        self.val=val
        self.next=next
        


class MyLinkedList:

    def __init__(self):
        self.head= None

    def get(self, index: int) -> int:
        temp=self.head
        
        while temp and index> 0:
            temp=temp.next
            index-=1

        return temp.val   if temp else -1 

    def addAtHead(self, val: int) -> None:
        
        temp=ListNode(val, self.head)
        self.head=temp

    def addAtTail(self, val: int) -> None:

        temp=self.head

        if not self.head:
            self.head= ListNode(val) 
            return 

        while temp.next:
            temp=temp.next

        temp.next= ListNode(val)    
     

    def addAtIndex(self, index: int, val: int) -> None:

        if index== 0:
            self.addAtHead(val)
            return
        else:

            temp= self.head

            while temp and index >1:
                temp=temp.next
                index-=1

            if not temp :
                return   

            new_node=ListNode(val, temp.next)
            temp.next=new_node            

    def deleteAtIndex(self, index: int) -> None:
        
        if not self.head:
            return

        if index==0:
            self.head= self.head.next
            return
        else:

            temp=self.head

            while temp.next and index>1:
                temp=temp.next
                index-=1

            if not temp.next:
                return     
            temp.next=temp.next.next   
            


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)