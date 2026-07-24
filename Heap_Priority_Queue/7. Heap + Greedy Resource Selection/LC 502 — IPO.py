from typing import List
import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        MaxProfit= []
        minCapital= [(c,p) for c, p in zip(capital,profits)]
        heapq.heapify(minCapital)

        for i in range(k):

            while minCapital and minCapital[0][0] <= w:
                capita, profit =heapq.heappop(minCapital)
                heapq.heappush(MaxProfit, - profits)
                
            
            
            w+= -heapq.heappop(MaxProfit)

        return w
            



        