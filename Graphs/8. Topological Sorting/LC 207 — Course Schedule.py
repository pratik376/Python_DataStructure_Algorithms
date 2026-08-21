from typing import List

from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:


        adjList= defaultdict(list)

        degree= defaultdict(int)

        for a,b in prerequisites:

            adjList[b].append(a)
            degree[a] +=1

        answer=[]

        q=deque()

        def bfs(q):

            while q:

                node = q.popleft()
                answer.append(node)

                for nei in adjList[node]:

                    degree[nei]-=1

                    if degree[nei]==0:
                        q.append(nei)

        for i in range(numCourses):

            if degree[i]==0:
                q.append(i)

        bfs(q)
        return len(answer)==numCourses

    

        