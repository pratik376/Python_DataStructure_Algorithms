from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        nums= [ -x for x in nums] # O(n) for space and O(n) for time

        heapq.heapify(nums) # O(n)

        while k>0:
            element= heapq.heappop(nums) # (logn)
            k-=1
        return -element
    
    # total time O(n + k * logn ) space is O(n)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

       heap=[]

       for num in nums:
           heapq.heappush(heap,num)

           if len(heap)> k:
               heapq.heappop(heap)
       return heap[0]
        
       
    
    # total time O(n + k * logn ) space is O(n)