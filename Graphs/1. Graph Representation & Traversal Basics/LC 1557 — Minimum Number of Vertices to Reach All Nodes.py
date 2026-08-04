from typing import List
from collections import defaultdict

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        inComingEdge= defaultdict(int)
      
        count=0
        vertex=-1
        
        for a, b in edges:
      
            inComingEdge[b]+=1

        for i in range(n):

            if inComingEdge[i]==0:
                count+=1
                vertex=i

            if count>1:
                return -1

        return vertex

        

    from typing import List

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        incoming = [0] * n

        for src, dst in edges:
            incoming[dst] += 1

        champions = []
        for i, incoming_cnt in enumerate(incoming):
            if incoming_cnt == 0:
                champions.append(i)

        if len(champions) != 1:
            return -1

        return champions[0]
        