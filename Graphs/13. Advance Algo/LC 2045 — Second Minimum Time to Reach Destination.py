from typing import List

from collections import defaultdict, deque
class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        adj=defaultdict(list)

        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)

        q=deque([1])
        curr_time=0
        res=-1
        visit_times= defaultdict(list) 

        while q:

            for i in range(len(q)):
                node= q.popleft()

                if node==n:

                    if res!=-1:
                        return curr_time
                    res=curr_time

                for nei in adj[node]:

                    nei_times=visit_times[nei]

                    if len(nei_times)==0 or (len(nei_times)==1 and nei_times[0] != curr_time):
                        q.append(nei)
                        nei_times.append(curr_time)

            if (curr_time // change) % 2 ==1:
                curr_time+= change -(curr_time % change)

            curr_time+=time

        

        