from typing import List
from collections import defaultdict, deque

class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        adj= defaultdict(list)

        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)


        res=0

        def dfs(curr,parent):

            total= values[curr]

            for nei in adj[curr]:

                if nei != parent:
                    total += dfs(nei,curr)

            if total %k ==0:
                res +=1

            return total

        dfs(0,-1)
        return res

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
        
        