from typing import List

from collections import defaultdict, deque
class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:

        adj= defaultdict(list)

        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited= set()



        def dfs(start):

            stack=[start]
            time=0 
            visited.add((start,time))

            while stack:

                node= stack.pop()
                
        