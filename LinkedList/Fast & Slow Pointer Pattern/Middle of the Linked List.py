# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:


        temp= head
        number_node= self.count_nodes(temp)
        n= number_node//2


        for _ in range(n):

            head=head.next

        return head            


    def count_nodes(self, temp):

        count=0

        while temp:

            count+=1
            temp= temp.next

        return count    



# optimal



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:


        fast=head
        slow= head

        while fast and fast.next :
            fast= fast.next.next
            slow= slow.next

        return slow    
