from typing import List
from collections import defaultdict


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        N = len(isConnected)
        adjency = defaultdict(list)

        for i in range(N):
            for j in range(N):

                if i == j:
                    continue

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

