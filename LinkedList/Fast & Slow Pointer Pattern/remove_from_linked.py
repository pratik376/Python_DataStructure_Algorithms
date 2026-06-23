# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        temp=head

        N= self.countNode(temp)

        if n==N:
            return head.next

        for _ in range(N-n-1 ):

            temp=temp.next
        
        nextPtr= temp.next

        temp.next=nextPtr.next

        return head     
        
    def countNode(self,temp):

        count=0

        while temp:
            count+=1
            temp= temp.next
            
        return count        

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy= ListNode(0,head)

        left, right= dummy, head

        while n >0 and right:
            right=right.next
            n-=1

        while right:

            right=right.next
            left=left.next

        left.next= left.next.next

        return dummy.next


