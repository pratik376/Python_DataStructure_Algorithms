from typing import List
from collections import defaultdict

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        inComingEdge= defaultdict(int)
      
        count=0
        vertex=0
        
        for a, b in edges:
      
            inComingEdge[b]+=1

        for i in range(n):

            if inComingEdge[i]==0:
                count+=1
                vertex=i

            if count>1:
                return -1

        return vertex

        

    
        