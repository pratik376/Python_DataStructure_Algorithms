from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        ROWS, COLUMNS= len(grid), len(grid[0])

        directions= [(1,0),(-1,0),(0,1),(0,-1)]

        answer=0
        visited= set()
        

        def dfs(i,j):

            stack=[(i,j)]
            if (i,j) not in visited and grid[i][j]==1:
                cell_count+=1
            visited.add((i,j))
            cell_count=0
          

            while stack:

                i, j = stack.pop()

                for R,C in directions:
                    nR, nC= i+R, j+C

                    if nR < 0 or nC< 0 or nR==ROWS or nC==COLUMNS or (nR,nC) in visited or grid[nR][nC]==0:
                        continue

                    visited.add((nR,nC))
                    stack.append((nR,nC))
                    cell_count+=1
            return cell_count


        for i in range(ROWS):

            for j in range(COLUMNS):

                if (i,j) not in visited and grid[i][j] !=0:

                    answer=max(answer,dfs(i,j))

        return answer

             




        
        