from typing import List
import heapq

class Solution:
    def minSum(self, arr: List[int]) -> int:
        
        
        num1=0
        num2=0
        

        heapq.heapify(arr)

        while len(arr)>1:

            n1= heapq.heappop(arr)
            n2= heapq.heappop(arr)

            num1 = num1 *10 + n1
            num2 =num2 *10 +n2        
        n1= heapq.heappop(arr)
        num1 = num1 * 10 + n1

        return num1 + num2

