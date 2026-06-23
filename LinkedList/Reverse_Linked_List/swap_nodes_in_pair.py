# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy= ListNode(0,head)
        prev, current= dummy, head


        while current and current.next:

            # save the pointer
            nxtPair= current.next.next 

            second=current.next

            # updates value

            second.next=current
            current.next=nxtPair
            prev.next= second

            # update ptr
            prev=current
            current= nxtPair

        return dummy.next    

