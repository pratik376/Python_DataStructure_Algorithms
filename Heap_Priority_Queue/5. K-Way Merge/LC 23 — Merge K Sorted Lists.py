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

            if lists[i]:

                # If two nodes have the same val, Python will compare the second item, which is a ListNode. ListNode objects are not naturally comparable, so this can raise an error.
                # heapq.heappush(heap, (lists[i].val,lists[i],i))  # value ,node, list number
                heapq.heappush(heap, (lists[i].val,i,lists[i])) 
                                                                 
        
        while heap:

            val, curr, list_index = heapq.heappop(heap)

            if not head:
                head=curr
            
            if not prev:
                prev=curr
            else:
                prev.next = curr
                prev=curr
            
            if curr.next:

                heapq.heappush(heap, (curr.next.val,list_index,curr.next))
        
        return head
            

            

        






        
