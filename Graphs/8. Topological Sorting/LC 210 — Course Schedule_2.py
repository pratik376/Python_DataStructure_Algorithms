from typing import List

from collections import deque, defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        answer=[]
        q=deque()
        adj= defaultdict(list)
        degree=defaultdict(int)


        for a, b in prerequisites:

            adj[b].append(a)
            degree[a]+=1

        def bfs(q):

            while q:

                node=q.popleft()
                answer.append(node)

                for nei in adj[node]:

                    degree[nei]-=1

                    if degree[nei]==0:
                        q.append(nei)

        for i in range(numCourses):

            if degree[i]==0:

                q.append(i)

        bfs(q)

        return answer if len(answer)== numCourses else []



        