from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:


        N= len(isConnected)
        directions= [(1,0),(-1,0),(0,1),(0,-1)]
        visited=set()
        province=0

        def dfs(i,j):

            stack=[(i,j)]
            visited.add((i,j))

            while stack:

                i, j = stack.pop()

                for r,c in directions:

                    nR,nC= r+i, c+j
                    








        for i in range(N):
            for j in range(N):

                if isConnected[i][j]==1 and (i,j) not in visited:

                    DFS(i,j)
                    province+=1

        return province

        