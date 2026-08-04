from typing import List
from collections import defaultdict

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        inComingEdge= defaultdict(int)
        outGoingEdge= defaultdict(int)

        for a, b in edges:
            outGoingEdge[a]+=1
            inComingEdge[b]+=1

    
        