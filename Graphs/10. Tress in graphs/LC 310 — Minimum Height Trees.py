from collections import defaultdict, deque
from typing import List

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        if n==1:
            return [0]

        adj= defaultdict(list)

        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        edge_count={}
        leaves= deque()

        for src, neighbours in adj.items():

            if len(neighbours)==1:
                leaves.append(src)

            edge_count[src]= len(neighbours)

        while leaves:

            if n<=2:
                return list(leaves)

            node=leaves.popleft()
            n-=1
            for nei in adj[node]:
                edge_count[nei] -=1

                if edge_count[nei]==1:
                    leaves.append(nei)

        