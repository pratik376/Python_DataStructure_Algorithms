from typing import List
from collections import defaultdict
import heapq


class Solution:
    def findAllPeople(
        self,
        n: int,
        meetings: List[List[int]],
        firstPerson: int
    ) -> List[int]:

        adj = defaultdict(list)

        for a, b, time in meetings:
            adj[a].append((b, time))
            adj[b].append((a, time))


        # time person learned secret, person
        heap = [
            (0, 0),
            (0, firstPerson)
        ]

        visited = set()


        while heap:

            time, person = heapq.heappop(heap)

            if person in visited:
                continue

            visited.add(person)


            for nei, meeting_time in adj[person]:

                if nei in visited:
                    continue

                # meeting already happened before
                # this person knew the secret
                if meeting_time < time:
                    continue

                heapq.heappush(
                    heap,
                    (meeting_time, nei)
                )


        return list(visited)