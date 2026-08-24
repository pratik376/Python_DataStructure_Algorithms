from typing import List
from collections import defaultdict, deque


class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:

        adj = defaultdict(list)
        indegree = defaultdict(int)
        q = deque()

        for a, b in relations:
            adj[a].append(b)
            indegree[b] += 1

        time.insert(0, 0)

        # Latest finishing time among all prerequisites
        # of a particular course
        prereq_time = [0] * (n + 1)

        answer = 0

        def bfs(q):
            nonlocal answer

            while q:

                course, current_time = q.popleft()

                answer = max(answer, current_time)

                for nei in adj[course]:

                    # nei may have multiple prerequisites.
                    # Remember the prerequisite that finishes latest.
                    prereq_time[nei] = max(
                        prereq_time[nei],
                        current_time
                    )

                    indegree[nei] -= 1

                    # All prerequisites of nei are finished
                    if indegree[nei] == 0:

                        q.append((
                            nei,
                            prereq_time[nei] + time[nei]
                        ))

        for i in range(1, n + 1):

            if indegree[i] == 0:
                q.append((i, time[i]))

        bfs(q)

        return answer