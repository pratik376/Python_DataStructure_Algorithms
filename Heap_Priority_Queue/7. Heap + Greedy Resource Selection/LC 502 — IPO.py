from typing import List
import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        MaxProfit= []
        minCapital= [(c,p) for c, p in zip(capital,profits)]
        heapq.heapify(minCapital)

        


        