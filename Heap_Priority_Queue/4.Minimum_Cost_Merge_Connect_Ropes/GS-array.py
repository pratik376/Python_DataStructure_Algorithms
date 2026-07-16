from typing import List
import heapq

class Solution:
    def minSum(self, arr: List[int]) -> int:
        
        
        num1=0
        num2=0
        mul_factor=1


        heapq.heapify(arr)

        while arr:
            