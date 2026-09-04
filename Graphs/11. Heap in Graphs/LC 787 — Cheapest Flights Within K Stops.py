from typing import List
from collections import deque, defaultdict


class Solution:
    def findCheapestPrice(
        self,
        n: int,
        flights: List[List[int]],
        src: int,
        dst: int,
        k: int
    ) -> int:

        adj = defaultdict(list)

        for a, b, cost in flights:
            adj[a].append((b, cost))

        # node, cost, remaining stops
        q = deque([(src, 0, k)])

        answer = float("inf")

        # (node, remaining stops) -> cheapest cost
        best = {}

        best[(src, k)] = 0

        while q:

            node, cost, stops = q.popleft()

            # We used too many stops.
            # dst is still allowed because k stops means k+1 flights.
            if stops < 0 and node != dst:
                continue

            if node == dst:
                answer = min(answer, cost)
                continue

            # No reason to explore if this path
            # is already more expensive than our answer.
            if cost >= answer:
                continue

            for nei, nei_cost in adj[node]:

                new_cost = cost + nei_cost
                new_stops = stops - 1

                # If this exact state was reached cheaper before,
                # don't process the worse version.
                if ((nei, new_stops) in best and best[(nei, new_stops)] <= new_cost):
                    continue

                best[(nei, new_stops)] = new_cost

                q.append(
                    (nei, new_cost, new_stops)
                )

        return answer if answer != float("inf") else -1


    from typing import List


class Solution:
    def findCheapestPrice(
        self,
        n: int,
        flights: List[List[int]],
        src: int,
        dst: int,
        k: int
    ) -> int:

        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1):

            tmpPrices = prices.copy()

            for s, d, p in flights:

                if prices[s] == float("inf"):
                    continue

                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p

            prices = tmpPrices

        return -1 if prices[dst] == float("inf") else prices[dst]