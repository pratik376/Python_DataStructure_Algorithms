from typing import List
from collections import defaultdict

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        adj = defaultdict(list)

        # Store (neighbor, original edge index)
        for index, (a, b) in enumerate(edges):
            adj[a].append((b, index))
            adj[b].append((a, index))

        visited = set()

        # parent[node] = (parent_node, edge_index_used_to_reach_node)
        parent = {}

        cycle_edges = []

        def dfs(start):

            stack = [(start, -1, 0)]
            visited.add(start)

            while stack:

                node, par, next_index = stack[-1]

                # Finished processing this node
                if next_index == len(adj[node]):
                    stack.pop()
                    continue

                # Update which neighbor we'll examine next
                stack[-1] = (node, par, next_index + 1)

                nei, edge_index = adj[node][next_index]

                # Ignore edge back to parent
                if nei == par:
                    continue

                if nei not in visited:

                    visited.add(nei)
                    parent[nei] = (node, edge_index)
                    stack.append((nei, node, 0))

                else:
                    # Found cycle:
                    # node ----> nei
                    cycle_edges.append(edge_index)

                    # Walk backward from node until we reach nei
                    curr = node

                    while curr != nei:
                        prev, parent_edge_index = parent[curr]
                        cycle_edges.append(parent_edge_index)
                        curr = prev

                    return True

            return False

        # Nodes are labeled 1...n
        parent[1] = (-1, -1)
        dfs(1)

        # Return cycle edge appearing latest in input
        latest_index = max(cycle_edges)

        return edges[latest_index]