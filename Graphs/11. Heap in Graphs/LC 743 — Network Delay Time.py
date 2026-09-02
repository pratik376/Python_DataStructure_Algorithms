from typing import List
from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:


        adj= defaultdict(list)

        for a,b, w in times:
            adj[a].append((b,w))

        answer=0
        visited= set()
        min_Heap=[ (0,k)]
        

        while min_Heap:

            w1, node= heapq.heappop(min_Heap)

            if node in visited:
                continue

            answer= max(answer,w1)

            visited.add(node)

            for n2,w2 in adj[node]:

                if n2 not in visited:
                    heapq.heappush(min_Heap, (w1+w2,n2))

        return -1 if len(visited)!=n else answer

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:


        adj= defaultdict(list)

        for a,b, w in times:
            adj[a].append((b,w))

        answer=0
        visited= set()
        min_Heap=[ (0,k)]
        visited.add(k)
        

        while min_Heap:

            w1, node= heapq.heappop(min_Heap)


            answer= max(answer,w1)

            visited.add(node)

            for n2,w2 in adj[node]:

                if n2 not in visited:
                    heapq.heappush(min_Heap, (w1+w2,n2))
                    visited.add(n2)

        return -1 if len(visited)!=n else answer

    



        