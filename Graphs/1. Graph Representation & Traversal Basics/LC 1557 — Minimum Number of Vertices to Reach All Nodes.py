from typing import List
from collections import defaultdict


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:

        incomingEdge= defaultdict(int)


        for a,b in edges:

            incomingEdge[b]+=1
        
        