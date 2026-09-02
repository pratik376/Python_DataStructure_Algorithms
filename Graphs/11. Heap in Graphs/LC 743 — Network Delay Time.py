from typing import List
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:


        adj= defaultdict(list)

        for a,b, w in times:
            adj[b].append((b,w))

        answer=0
        visited= set()

        def dfs(node,time):

            stack=[node]
            visited.add(node)

            while stack:
                node, time =stack.pop()

                answer= max(answer,time)

                for nei, nei_time in adj[node]:

                    if nei not in visited:
                        visited.add(nei)
                        stack.append((nei,nei_time ))

            return answer



        