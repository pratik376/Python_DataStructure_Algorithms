from typing import List

class Solution:
    def minDays(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def countIslands():

            visited = set()
            islands = 0

            def dfs(r, c):

                stack = [(r, c)]
                visited.add((r, c))

                while stack:

                    r, c = stack.pop()

                    for dr, dc in directions:

                        nr, nc = r + dr, c + dc

                        if (
                            nr < 0 or nr >= ROWS or
                            nc < 0 or nc >= COLS or
                            (nr, nc) in visited or
                            grid[nr][nc] == 0
                        ):
                            continue

                        visited.add((nr, nc))
                        stack.append((nr, nc))

            for r in range(ROWS):
                for c in range(COLS):

                    if grid[r][c] == 1 and (r, c) not in visited:
                        islands += 1
                        dfs(r, c)

            return islands


        # Already disconnected
        if countIslands() != 1:
            return 0


        # Try removing every land cell individually
        for r in range(ROWS):
            for c in range(COLS):

                if grid[r][c] == 0:
                    continue

                # Temporarily remove this land
                grid[r][c] = 0

                # Did this removal disconnect the island?
                if countIslands() != 1:
                    grid[r][c] = 1
                    return 1

                # Restore before testing another cell
                grid[r][c] = 1


        # No single removal worked
        return 2