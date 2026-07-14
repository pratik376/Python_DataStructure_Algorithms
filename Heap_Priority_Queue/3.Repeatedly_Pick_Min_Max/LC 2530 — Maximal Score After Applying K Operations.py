from typing import List
import heapq

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:

        heap= [ -val for val in nums]

        heapq.heapify(heap)

        score=0

        for _ in range(k):
            


        