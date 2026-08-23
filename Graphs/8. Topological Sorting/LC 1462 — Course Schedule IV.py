from typing import List
from collections import defaultdict, deque

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
       
        adj= defaultdict(list)
        proven_pair=set()
     

        for u, v in prerequisites:

            adj[u].append(v)

        def dfs(source,target,visited):

            stack=[source]
            visited.add(source)

            while stack:

                node= stack.pop()

                proven_pair.add((source,node))

                if node == target:
                    return True
                              
                for nei in adj[node]:

                    if nei not in visited:
                        visited.add(nei)
                        stack.append(nei)

            return False            
       
        answer=[False] * len(queries)
        for i in range(len(queries)):  

            if (queries[i][0], queries[i][1]) in proven_pair or dfs(queries[i][0],queries[i][1],set()) :
                answer[i]=True

        return answer




        





        