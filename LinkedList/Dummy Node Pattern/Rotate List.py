# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        

        if not head or not head.next or k==0:
            return head
        
        dummy =ListNode(-1,head)
        
        temp=head
        N=self.countNode(temp)

        k=k%N

        if k==0:
            return head

        slow=fast=head

        while k>0 and fast.next:

            fast=fast.next
            k-=1

        while fast.next:
            fast=fast.next
            slow=slow.next


        dummy.next= slow.next
        fast.next=head
        slow.next=None

        return dummy.next    
                

    def countNode(self,temp):
        my_count=0

        while temp:
            my_count+=1
            temp=temp.next

        return my_count    






from typing import Optional

# 95%
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        n = self.countNode(head)
        k %= n

        if k == 0:
            return head

        slow = fast = head

        while k > 0:
            fast = fast.next
            k -= 1

        while fast.next:
            fast = fast.next
            slow = slow.next

        new_head = slow.next
        slow.next = None
        fast.next = head

        return new_head

    def countNode(self, temp):
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count