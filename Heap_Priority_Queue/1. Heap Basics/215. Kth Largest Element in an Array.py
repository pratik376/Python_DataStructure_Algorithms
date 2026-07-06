from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        nums= [ -x for x in nums]

        heapq.heapify(nums)

        while k>0:
            element= heapq.heappop(nums)
            k-=1
        return -element
        