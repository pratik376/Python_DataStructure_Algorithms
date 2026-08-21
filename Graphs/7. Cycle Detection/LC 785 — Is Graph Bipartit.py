from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        visited=set()
        status={}




        def dfs(node):
            stack=[node]
            status[node]="A"
            visited.add(node)
            while stack:

                node=stack.pop()

                for nei in graph[node]:

                    if nei not in visited:

                        if status[node]=="A":
                            status[nei]="B"
                        else:
                            status[nei]="A"

                        stack.append(nei)
                        visited.add(nei)
                    elif status[node]==status[nei]:
                        return False
            return True

        for i in range(len(graph)):
            if i not in visited:
                if not dfs(i):
                    return False
        return True
                      

                


        
        






        