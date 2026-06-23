# Definition for singly-linked list.
from typing import Optional

# double nahi system thi ek ek kapvanu

# use if else and handle things differently based on the situation
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy= ListNode(head)

        prev= dummy

# 85 %

        while head:

            if head.next and head.val== head.next.val:

                while head.next and head.val == head.next.val:
                 head=head.next

                prev.next=head.next
            else:
                prev= head.next    

            head=head.next

        return dummy.next         


        