# Definition for singly-linked list.
from typing import Optional

# think carefully about the pointers
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        fast, slow= head, head

        
        # finding the middle element
        while fast and fast.next :
            
            fast= fast.next.next
            slow= slow.next

        # reversing for the middle middle
        
        second= slow.next
        prev=slow.next=None
        
        
        while second:
            nextPtr=second.next
            second.next=prev    
            prev=second
            second=nextPtr

        left, right= head, prev

        while right:

            temp1, temp2= left.next, right.next

            left.next= right
            right.next=temp1

            left= temp1
            right= temp2


            
        