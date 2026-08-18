from typing import List
from collections import deque

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:

 
        visited=set()
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        N= len(grid)
        q=deque()


        def dfs(i,j):

            stack=[(i,j)]
            q.append((i,j,0))
            visited.add((i,j))


            while stack:

                i, j = stack.pop()

                for r,c in directions:

                    nR,nC= i+r, j+c

                    if nR < 0 or nC <0 or nR>=N or nC>=N or (nR,nC) in visited or grid[nR][nC]==0:
                        continue

                    stack.append((nR,nC))
                    q.append((nR,nC,0))
                    visited.add((nR,nC))

        found=False
        for i in range(N):

            if found:
                break

            for j in range(N):

                if grid[i][j]==1:
                    dfs(i,j)
                    found=True
                    break


        while q:

            i, j, dist= q.popleft()

           

            for r,c in directions:
                nR,nC= i+r, j+c

                

                if nR < 0 or nC <0 or nR>=N or nC>=N or (nR,nC) in visited:
                    continue
                if grid[nR][nC]==1:
                    return dist
                q.append((nR,nC,dist+1))
                visited.add((nR,nC))


        # time and spce O(n2)



            
        