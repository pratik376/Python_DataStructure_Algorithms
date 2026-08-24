from typing import List
from collections import defaultdict
# path.remove()

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:

        adj= defaultdict(list)

        for a,b in edges:
            adj[a].append(b)

        visited =set()
        isCycle=False
        answer= 0

        def dfs(node, path,color_count):
            nonlocal isCycle
            nonlocal answer

            if node in visited:
                color_count[colors[node]]+=1

                answer=max(answer, max(color_count.values))

                return

            if node in path:
                isCycle=True
                return
            path.add(node)
            color_count[colors[node]]+=1

            for nei in adj[node]:

                dfs(nei,path,color_count)
                answer= max(answer, max(color_count.values))

                color_count= defaultdict(int)
                color_count[colors[node]]+=1

            visited.add(node)
            path.remove(node)


        for  i in range(len(colors)):

            if i not in visited:

                if not isCycle:
                    color_count= defaultdict(int)
                    dfs(i, set(), color_count)
                else:
                    return -1

        return answer
                


     



from typing import List
from collections import defaultdict


class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:

        adj = defaultdict(list)

        for a, b in edges:
            adj[a].append(b)

        N = len(colors)

        visited = set()
        path = set()

        # count[node][color]
        # maximum frequency of that color
        # on a path starting from this node
        count = [[0] * 26 for _ in range(N)]

        isCycle = False
        answer = 0

        def dfs(node):

            nonlocal isCycle
            nonlocal answer

            if node in path:
                isCycle = True
                return

            # Already completely calculated
            if node in visited:
                return

            path.add(node)

            for nei in adj[node]:

                dfs(nei)

                if isCycle:
                    return

                # Take the best result from this child
                for color in range(26):

                    count[node][color] = max(
                        count[node][color],
                        count[nei][color]
                    )

            # Add current node's own color
            current_color = ord(colors[node]) - ord('a')

            count[node][current_color] += 1

            # Best color count starting from this node
            answer = max(
                answer,
                max(count[node])
            )

            # Done processing this node
            path.remove(node)
            visited.add(node)

        for i in range(N):

            if i not in visited:
                dfs(i)

            if isCycle:
                return -1

        return answer