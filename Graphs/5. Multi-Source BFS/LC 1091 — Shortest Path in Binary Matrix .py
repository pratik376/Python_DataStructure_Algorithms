from typing import List

from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        N=len(grid)

        if grid[0][0] == 1 or grid[N-1][N-1]==1:
            return -1

        visited = set()

        directions = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]

        res = 0
        # space complexity = O(n2)
        # time complexity = O(V+E) -> v= N**2 and E= 8 * N **2
        q=deque()

        q.append((0,0,1))

        visited.add((0,0))

        while q:
            i,j, dist=q.popleft()

            if i == N-1 or j==N-1:
                return dist

            for r,c in directions:
                nR,nC= r+i, j+c

                if nR < 0 or nC <0 or nR>=N or nC>=N or (nR,nC) in visited or grid[nR][nC]==1:
                    continue
                visited.add((nR,nC))
                q.append((nR,nC,dist+1))

        return -1


