# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        if not head:
            return False
        
        fast=head
        slow=head

        # finding the middle

        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next

        # reversing from the middle

        prev=None

        while slow:
            nextPtr=slow.next
            slow.next=prev
            prev  = slow
            slow= nextPtr

        left, right= head, prev

        while right:

            if left.val != right.val:
             return False

            right= right.next
            left= left.next

        return True            
        

        

        