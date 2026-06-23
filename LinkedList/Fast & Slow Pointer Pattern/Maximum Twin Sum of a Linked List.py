# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:


        fast= head
        slow=head


       # find the middle

        while fast and fast.next :

            fast= fast.next.next
            slow= slow.next
       
       # now reverse

        prev=None

        while slow:

            nextPtr=slow.next
            slow.next=prev
            prev=slow
            slow= nextPtr


        # finiding the sum


        left, right= head, prev

        window_sum=float('-inf')

        while right:

            window_sum= max(window_sum,(left.val+ right.val))

            left=left.next
            right=right.next

        return window_sum    



        