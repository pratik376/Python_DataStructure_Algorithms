from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        ROWS, COLUMNS = len(grid), len(grid[0])

        visited = set()
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(i, j):

            stack = [(i, j)]
            visited.add((i, j))

            perimeter = 0

            while stack:

                i, j = stack.pop()

                for R, C in directions:

                    nR, nC = i + R, j + C

                    # Neighbor is outside the grid
                    if (
                        nR < 0 or nC < 0 or
                        nR >= ROWS or nC >= COLUMNS
                    ):
                        perimeter += 1
                        continue

                    # Neighbor is water
                    if grid[nR][nC] == 0:
                        perimeter += 1
                        continue

                    # Neighbor is land but already visited
                    if (nR, nC) in visited:
                        continue

                    # Neighbor is new land
                    visited.add((nR, nC))
                    stack.append((nR, nC))

            return perimeter

        for i in range(ROWS):
            for j in range(COLUMNS):

                if grid[i][j] == 1 and (i, j) not in visited:
                    return dfs(i, j)

        return 0

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visit = set()

        def dfs(i, j):
            if i >= len(grid) or j >= len(grid[0]) or \
               i < 0 or j < 0 or grid[i][j] == 0:
                return 1

            if (i, j) in visit:
                return 0

            visit.add((i, j))

            perim = dfs(i, j + 1)
            perim += dfs(i + 1, j)
            perim += dfs(i, j - 1)
            perim += dfs(i - 1, j)

            return perim

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    return dfs(i, j)