from typing import List

class Solution:
    def numDistinctIslands2(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])

        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        visited = set()
        shapes = set()

        def normalize(shape):

            # 8 possible transformations
            transformations = [[] for _ in range(8)]

            for r, c in shape:

                transformations[0].append(( r,  c))
                transformations[1].append(( r, -c))
                transformations[2].append((-r,  c))
                transformations[3].append((-r, -c))

                transformations[4].append(( c,  r))
                transformations[5].append(( c, -r))
                transformations[6].append((-c,  r))
                transformations[7].append((-c, -r))

            normalized = []

            for transformation in transformations:

                transformation.sort()

                # Remove location/translation again
                startR, startC = transformation[0]

                current = []

                for r, c in transformation:
                    current.append((r - startR, c - startC))

                normalized.append(tuple(current))

            # Every rotated/reflected version of the same island
            # will produce the same minimum representation.
            return min(normalized)


        def dfs(i, j):

            startR, startC = i, j

            stack = [(i, j)]
            visited.add((i, j))

            shape = []

            while stack:

                i, j = stack.pop()

                # Your LC 694 idea
                shape.append((i - startR, j - startC))

                for dr, dc in directions:

                    nR, nC = i + dr, j + dc

                    if (
                        nR < 0 or nR >= ROWS or
                        nC < 0 or nC >= COLS or
                        (nR, nC) in visited or
                        grid[nR][nC] == 0
                    ):
                        continue

                    visited.add((nR, nC))
                    stack.append((nR, nC))

            return normalize(shape)


        for i in range(ROWS):
            for j in range(COLS):

                if grid[i][j] == 1 and (i, j) not in visited:

                    shape = dfs(i, j)

                    shapes.add(shape)

        return len(shapes)