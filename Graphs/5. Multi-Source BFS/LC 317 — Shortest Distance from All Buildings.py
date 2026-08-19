from typing import List
from collections import deque

class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])

        directions = [
            (1,0),
            (-1,0),
            (0,1),
            (0,-1)
        ]

        # Sum of distances from all buildings
        distance = [[0] * COLS for _ in range(ROWS)]

        # How many buildings were able to reach this cell
        reach = [[0] * COLS for _ in range(ROWS)]

        total_buildings = 0

        def bfs(i, j):

            visited = set()
            q = deque()

            q.append((i, j, 0))
            visited.add((i, j))

            while q:

                i, j, dist = q.popleft()

                for r, c in directions:

                    nR, nC = i + r, j + c

                    if (
                        nR < 0 or nC < 0 or
                        nR >= ROWS or nC >= COLS or
                        (nR, nC) in visited or
                        grid[nR][nC] != 0
                    ):
                        continue

                    visited.add((nR, nC))

                    distance[nR][nC] += dist + 1
                    reach[nR][nC] += 1

                    q.append((nR, nC, dist + 1))


        # Run separate BFS from every building
        for i in range(ROWS):
            for j in range(COLS):

                if grid[i][j] == 1:
                    total_buildings += 1
                    bfs(i, j)


        answer = float("inf")

        # Find empty cell reached by EVERY building
        for i in range(ROWS):
            for j in range(COLS):

                if (
                    grid[i][j] == 0 and
                    reach[i][j] == total_buildings
                ):
                    answer = min(answer, distance[i][j])


        return answer if answer != float("inf") else -1