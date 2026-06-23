# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
         
        total=0
        mf=1 
        while l1:

            val= l1.val * mf
            total+=val
            mf *=10
            l1=l1.next


        mf=1

        while l2:
            val= l2.val * mf
            total+=val
            mf*=10
            l2=l2.next
        
        
        if total == 0:
         return ListNode(0)

        NumberNode=temp= None

        for digit in  str(total)[::-1]:

            if not NumberNode:
              NumberNode=ListNode(int(digit))
              temp=NumberNode
            else:

                new_node= ListNode(int(digit)) 
                temp.next=new_node
                temp=temp.next

        return   NumberNode         
    

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy= ListNode()

        cur= dummy
        carry= 0

        while l1 or l2 or carry:

            v1= l1.val if l1 else 0
            v2= l2.val if l2 else 0

            val= v1 + v2+ carry

            carry= val // 10
            val=val %10

            cur.next= ListNode(val)

            cur=cur.next

            l1=l1.next if l1 else None
            l2=l2.next if l2 else None

        return dummy.next    
            
        