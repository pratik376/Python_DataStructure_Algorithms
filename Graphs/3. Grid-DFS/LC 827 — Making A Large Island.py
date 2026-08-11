from typing import List

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:

        N = len(grid)
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        # island_id -> area
        area = {}

        # Start IDs at 2 because grid already uses 0 and 1
        island_id = 2


        def dfs(r, c, island_id):

            stack = [(r, c)]

            # Change 1 into this island's ID
            grid[r][c] = island_id

            size = 0

            while stack:

                r, c = stack.pop()
                size += 1

                for dr, dc in directions:

                    nr, nc = r + dr, c + dc

                    if (
                        nr < 0 or nr >= N or
                        nc < 0 or nc >= N or
                        grid[nr][nc] != 1
                    ):
                        continue

                    grid[nr][nc] = island_id
                    stack.append((nr, nc))

            return size


        # PHASE 1:
        # Find every island and give it a unique ID
        for r in range(N):
            for c in range(N):

                if grid[r][c] == 1:

                    area[island_id] = dfs(r, c, island_id)
                    island_id += 1


        # If there are already islands, this handles
        # the "don't need to flip" case
        answer = max(area.values(), default=0)


        # PHASE 2:
        # Try changing every 0 into a 1
        for r in range(N):
            for c in range(N):

                if grid[r][c] != 0:
                    continue

                # The flipped 0 itself
                new_area = 1

                # Avoid counting the same island twice
                neighboring_islands = set()

                for dr, dc in directions:

                    nr, nc = r + dr, c + dc

                    if (
                        nr < 0 or nr >= N or
                        nc < 0 or nc >= N
                    ):
                        continue

                    island = grid[nr][nc]

                    if island > 1:
                        neighboring_islands.add(island)

                for island in neighboring_islands:
                    new_area += area[island]

                answer = max(answer, new_area)


        return answer