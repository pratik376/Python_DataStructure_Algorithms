from typing import List

# my solution
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        ROWS, COLS= len(grid), len(grid[0])
        directions= [(1,0),(-1,0),(0,1),(0,-1)]

        visited= set()
        final_answer=0
        

        def dfs(i,j):
            answer=0
            stack=[(i,j)]
            visited.add((i,j))
            isBoundry=0

            if grid[i][j]==1 and (i==0 or i==ROWS-1) or (j==0 or j==COLS-1):
                isBoundry=1

            elif grid[i][j]==1 and ( 0<i and i<ROWS)  and ( 0<j and j < COLS):
                answer+=1

            while stack:
                i,j =stack.pop()

                for r,c in directions:

                    nR,nC= r+i, c+j

                    if nR < 0 or nC< 0 or nR==ROWS or nC==COLS or (nR,nC) in visited or grid[nR][nC]==0:
                        continue

                    if (nR==0 or nR==ROWS-1) or (nC==0 or nC==COLS-1):
                        isBoundry=True

                    if ( 0<nR and nR<ROWS)  and ( 0<nC and nC < COLS):
                        answer+=1
                    visited.add((nR,nC))
                    stack.append((nR,nC))

            return 0 if isBoundry else answer
    
        for i in range(ROWS):
            for j in range(COLS):

                if grid[i][j]==1 and not (i,j) in visited:
                    final_answer+=dfs(i,j)
        return final_answer


from typing import List

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        # Return num of land cells
        def dfs(r, c):
            if (r < 0 or c < 0 or
                r == ROWS or c == COLS or
                not grid[r][c] or (r, c) in visit):
                return 0

            visit.add((r, c))

            res = 1
            direct = [[0, 1], [0, -1], [1, 0], [-1, 0]]

            for dr, dc in direct:
                res += dfs(r + dr, c + dc)

            return res

        visit = set()
        land, borderLand = 0, 0

        for r in range(ROWS):
            for c in range(COLS):
                land += grid[r][c]

                if (grid[r][c] and
                    (r, c) not in visit and
                    (c in [0, COLS - 1] or r in [0, ROWS - 1])):

                    borderLand += dfs(r, c)

        return land - borderLand

# approved solution of original 
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        ROWS, COLS= len(grid), len(grid[0])
        directions= [(1,0),(-1,0),(0,1),(0,-1)]

        visited= set()
        final_answer=0
        

        def dfs(i,j):
            answer=0
            stack=[(i,j)]
            visited.add((i,j))
            isBoundry=0
            count=0

           

            while stack:
                i,j =stack.pop()

                count+=1 # of current
                if (i==0 or i==ROWS-1) or (j==0 or j==COLS-1):
                    isBoundry=1
                if ( 0<i and i<ROWS)  and ( 0<j and j < COLS):
                    count+=1

                for r,c in directions:

                    nR,nC= r+i, c+j

                    if nR < 0 or nC< 0 or nR==ROWS or nC==COLS or (nR,nC) in visited or grid[nR][nC]==0:
                        continue
                    
                    visited.add((nR,nC))
                    stack.append((nR,nC))

            return 0 if isBoundry else answer
    
        for i in range(ROWS):
            for j in range(COLS):

                if grid[i][j]==1 and not (i,j) in visited:
                    final_answer+=dfs(i,j)
        return final_answer
