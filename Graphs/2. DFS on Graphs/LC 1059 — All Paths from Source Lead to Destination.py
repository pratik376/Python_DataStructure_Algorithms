from typing import List
from collections import defaultdict


class Solution:
    def leadsToDestination(
        self,
        n: int,
        edges: List[List[int]],
        source: int,
        destination: int
    ) -> bool:

        graph = defaultdict(list)

        for a, b in edges:
            graph[a].append(b)

        path = set()

        # (node, entering)
        stack = [(source, True)]

        while stack:

            node, entering = stack.pop()

            if entering:

                # Cycle
                if node in path:
                    return False

                # Leaf
                if not graph[node]:
                    if node != destination:
                        return False
                    continue

                path.add(node)

                # Come back later and remove node
                stack.append((node, False))

                for nei in reversed(graph[node]):
                    stack.append((nei, True))

            else:
                path.remove(node)

        return True