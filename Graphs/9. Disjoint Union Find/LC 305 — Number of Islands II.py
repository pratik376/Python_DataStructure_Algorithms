from typing import List


class Solution:
    def numIslands2(
        self,
        m: int,
        n: int,
        positions: List[List[int]]
    ) -> List[int]:

        parent = [-1] * (m * n)
        size = [1] * (m * n)

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        islands = 0
        answer = []

        def find(node):

            p = parent[node]

            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]

            return p

        def union(a, b):

            p1 = find(a)
            p2 = find(b)

            if p1 == p2:
                return False

            if size[p1] > size[p2]:
                parent[p2] = p1
                size[p1] += size[p2]

            else:
                parent[p1] = p2
                size[p2] += size[p1]

            return True

        for r, c in positions:

            node = r * n + c

            # This position was already turned into land
            if parent[node] != -1:
                answer.append(islands)
                continue

            # Create a new island
            parent[node] = node
            size[node] = 1
            islands += 1

            for dr, dc in directions:

                nr = r + dr
                nc = c + dc

                if nr < 0 or nc < 0 or nr >= m or nc >= n:
                    continue

                nei = nr * n + nc

                # Neighbor is water
                if parent[nei] == -1:
                    continue

                # Two different islands were merged
                if union(node, nei):
                    islands -= 1

            answer.append(islands)

        return answer