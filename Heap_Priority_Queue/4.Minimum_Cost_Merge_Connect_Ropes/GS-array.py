from typing import List
import heapq

class Solution:
    def minSum(self, arr: List[int]) -> int:
        
        cost=0

        heapq.heapify(arr)

        while 