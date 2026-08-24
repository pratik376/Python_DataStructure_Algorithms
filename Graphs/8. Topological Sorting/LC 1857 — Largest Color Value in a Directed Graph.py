from typing import List
from collections import defaultdict


class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:

        adj= defaultdict(list)

        for a,b in edges:
            adj[a].append(b)

        visited =set()
        isCycle=False

        def dfs(node, path,color_count):
            nonlocal isCycle

            if node in path:
                isCycle=True
                return
            path.add(node)
            color_count[colors[node]]+=1

            for nei in adj[node]:

                dfs(nei,path,color_count)

            visited.add(node)

        answer=0

        for  i in range(len(edges)):

            if i not in visited and not isCycle:
                color_count= defaultdict(int)
                dfs(i, set(), color_count)
                answer= max(answer, max(color_count.values))

        return answer
                


     




        