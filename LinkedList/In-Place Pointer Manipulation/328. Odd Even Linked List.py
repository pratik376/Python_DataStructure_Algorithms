# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        dummy = temp = ListNode()

        odd = head
        even = head.next

        # Add odd position nodes
        while odd:
            temp.next = odd
            temp = temp.next

            if odd.next:
                odd = odd.next.next
            else:
                odd = None

        # Add even position nodes
        while even:
            temp.next = even
            temp = temp.next

            if even.next:
                even = even.next.next
            else:
                even = None

        temp.next = None

        return dummy.next
    
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

      

        odd = head
        
        even_head= even=head.next

        while even and even.next:
            odd.next= odd.next.next
            odd=odd.next

            even.next=even.next.next
            even=even.next

        odd.next=even_head

        return head    
