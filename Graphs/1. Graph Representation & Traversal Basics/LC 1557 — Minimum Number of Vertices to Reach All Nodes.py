from typing import List
from collections import defaultdict


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:

        incomingEdge= defaultdict(int)
        answer=[]


        for a,b in edges:

            incomingEdge[b]+=1

        for i in range(n):

            if incomingEdge[i]==0:
                answer.append(i)

        return answer

        
        
        