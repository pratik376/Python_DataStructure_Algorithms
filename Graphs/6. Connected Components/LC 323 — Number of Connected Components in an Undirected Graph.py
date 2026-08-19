from typing import List
from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:


        adj= defaultdict(list)

        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited= set()
        answer=0

        def dfs(i):

            stack=[i]
            visited.add(i)

            while stack:
                node= stack.pop()

                for nei in adj[node]:

                    if nei is not visited:
                        stack.append(nei)
                        visited.add(nei)

        for i in range(len(edges)):

            if i not in visited:
                dfs(i)
                answer+=1

        return answer






        



