from typing import List

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])

        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        visited = set()
        shapes = set()

        def dfs(i, j):

            startR, startC = i, j
            shape = []

            stack = [(i,j)]
            visited.add((i,j))

            while stack:

                i, j = stack.pop()

                shape.append((i - startR, j - startC))

                for r, c in directions:

                    nR, nC = i + r, j + c

                    if (
                        nR < 0 or nC < 0 or
                        nR >= ROWS or nC >= COLS or
                        (nR,nC) in visited or
                        grid[nR][nC] == 0
                    ):
                        continue

                    visited.add((nR,nC))
                    stack.append((nR,nC))

            return tuple(sorted(shape))

        for i in range(ROWS):
            for j in range(COLS):

                if grid[i][j] == 1 and (i,j) not in visited:
                    shapes.add(dfs(i,j))

        return len(shapes)