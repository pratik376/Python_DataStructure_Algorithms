from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        visited=set()
        status={}
        status_A,status_B= "A","B"


        for node, neighbours in enumerate(graph):

            if node not in visited:
                status[node]="A"
                visited.add(node)

            for nei in neighbours:

                

                if nei not in visited:

                    if status[node]=="A":
                        status[nei]="B"
                       
                    else:
                        status[nei]="A"

                    visited.add(nei)

                elif status[node] == status[nei]:
                    return False

        return True






        