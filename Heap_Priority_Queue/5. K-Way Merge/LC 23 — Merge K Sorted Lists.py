# Definition for singly-linked list.
from typing import List, Optional

import heapq
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        prev=None
        heap=[]
        head=None

        for i in range(len(lists)):

            heapq.heappush(heap, (lists[i][0].val,lists[i][0],i,0))  # value ,node, list number, node_nuber
        
        while heap:

            val, curr, list_index, node_number = heapq.heappop(heap)

            if not head:
                head=curr
            
            if not prev:
                curr=prev
            else:
                prev.next = curr
                prev=curr
            
            if curr.next:

                heapq.heappush(heap, (lists[list_index][node_number+1].val,lists[list_index][node_number+1], list_index, node_number +1))
        
        return head
            

            

        






        
