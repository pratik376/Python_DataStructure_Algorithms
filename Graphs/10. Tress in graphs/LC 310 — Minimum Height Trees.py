from collections import defaultdict, deque
from typing import List

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        if n==1:
            return [0]

        adj= defaultdict(list)

        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        edge_count={}
        leaves= deque()

        for src, neighbours in adj.items():

            if len(neighbours)==1:
                leaves.append(src)

            edge_count[src]= len(neighbours)

        while leaves:

            if n<=2:
                return list(leaves)

            node=leaves.popleft()
            n-=1
            for nei in adj[node]:
                edge_count[nei] -=1

                if edge_count[nei]==1:
                    leaves.append(nei)
from collections import defaultdict, deque
from typing import List


class Solution:
    def maxKDivisibleComponents(
        self,
        n: int,
        edges: List[List[int]],
        values: List[int],
        k: int
    ) -> int:

        if n == 1:
            return 1

        adj = defaultdict(list)

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        edge_count = {}
        leaves = deque()

        for src, neighbours in adj.items():

            edge_count[src] = len(neighbours)

            if edge_count[src] == 1:
                leaves.append(src)

        node_sum = values[:]
        answer = 0

        while leaves:

            node = leaves.popleft()

            # Find the only remaining neighbour
            parent = -1

            for nei in adj[node]:

                if edge_count[nei] > 0:
                    parent = nei
                    break

            # Current component can be separated
            if node_sum[node] % k == 0:
                answer += 1

            # Otherwise it must remain connected
            # and contribute its sum to parent
            elif parent != -1:
                node_sum[parent] += node_sum[node]

            # Remove current leaf
            edge_count[node] = 0

            if parent != -1:

                edge_count[parent] -= 1

                if edge_count[parent] == 1:
                    leaves.append(parent)

        return answer