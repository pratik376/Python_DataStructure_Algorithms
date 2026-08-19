from typing import List
from collections import defaultdict


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        N = len(isConnected)
        adjency = defaultdict(list)

        for i in range(N):
            for j in range(N):

                if isConnected[i][j] == 1:
                    adjency[i].append(j)

        

        visited= set()
        answer=0

        def dfs(node):

            stack=[node]
            visited.add(node)

            while stack:

                node = stack.pop()

                for nei in adjency[node]:

                    if nei not in visited:
                        stack.append(nei)
                        visited.add(nei)

        for key in adjency.keys(): 

            if not key in visited:
                dfs(key)
                answer+=1

        return answer



class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        N= len(isConnected)
        visited=set()
        answer=0

        def dfs(city):

            stack=[city]
            visited.add(city)

            while stack:
                city=stack.pop()
            

                for nei in range(N):

                    if nei not in visited and isConnected[city][nei]==1:
                        visited.add(nei)
                        stack.append(nei)
                    
        for city in range(N):

            if city not in visited:
                dfs(city)
                answer+=1

        return answer




