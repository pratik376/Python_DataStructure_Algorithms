from typing import List
from collections import defaultdict, deque


class Solution:
    def minimumDiameterAfterMerge(
        self,
        edges1: List[List[int]],
        edges2: List[List[int]]
    ) -> int:

        def findDiameter(edges):

            n = len(edges) + 1

            if n == 1:
                return 0

            adj = defaultdict(list)

            for n1, n2 in edges:
                adj[n1].append(n2)
                adj[n2].append(n1)

            edge_count = {}
            leaves = deque()

            for src, neighbours in adj.items():

                edge_count[src] = len(neighbours)

                if len(neighbours) == 1:
                    leaves.append(src)

            layers = 0

            while leaves:

                if n <= 2:
                    break

                for _ in range(len(leaves)):

                    node = leaves.popleft()
                    n -= 1

                    for nei in adj[node]:

                        edge_count[nei] -= 1

                        if edge_count[nei] == 1:
                            leaves.append(nei)

                layers += 1

            # One center remaining
            if n == 1:
                diameter = layers * 2

            # Two centers remaining
            else:
                diameter = layers * 2 + 1

            return diameter

        diameter1 = findDiameter(edges1)
        diameter2 = findDiameter(edges2)

        radius1 = (diameter1 + 1) // 2
        radius2 = (diameter2 + 1) // 2

        cross_diameter = radius1 + 1 + radius2

        return max(
            diameter1,
            diameter2,
            cross_diameter
        )