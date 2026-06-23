
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        
        num_set= set(nums)

        while head and head.val in num_set:
            head=head.next

        current= head
        previous=None

        while current:

            if current.val in num_set:
                previous.next=current.next 
            else:
                previous=current      

            current=current.next     

        return head    

