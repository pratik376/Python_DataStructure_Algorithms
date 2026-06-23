
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return

        
        temp=head.next

       


        while temp:

            current=temp
            window_sum=0

            while current.val != 0:
                window_sum+= current.val
                current= current.next

            temp.val= window_sum
            temp.next=current.next
            temp=temp.next

        head=head.next

        return head            


        