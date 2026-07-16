from typing import List
import heapq

class Solution:
    def minSum(self, arr: List[int]) -> int:
        
        
        num1=0
        num2=0
        mul_factor=1


        heapq.heapify(arr)

        while len(arr)>1:

            n1= heapq.heappop(arr)
            n2= heapq.heappop(arr)

            num1 += (mul_factor *n1)
            num2 +=(mul_factor *n2)

            mul_factor *=10
        n1= heapq.heappop(arr)
        num1 += (mul_factor *n1)

        return num1 + num2

