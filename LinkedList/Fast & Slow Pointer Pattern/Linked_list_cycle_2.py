# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

       
       if not head:
        return None
       
       visited= set()
       
       curr= head

       while curr:

        if curr in visited:
           return curr
        else:
           visited.add(curr)

        curr=curr.next   

        return None    


# this is  the optimal solution
#  0(1)  space and 0(1) time




class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

       
       if not head:
        return None
       
       fast=head
       slow=head

       while fast and fast.next :

        slow= slow.next
        fast= fast.next.next

        if slow == fast:
           
           slow= head

           while slow != fast :
              
              slow=slow.next
              fast= fast.next

           return slow  
       
      
       return None    
        