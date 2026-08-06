
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None

        oldToNew={}
        oldToNew[node]=Node(node.val)
       

        stack=[node]

        while stack:

            curr = stack.pop()

            for nei in curr.neighbors:

                if nei not in oldToNew:
                    oldToNew[nei]=Node(nei.val)
                    stack.append(nei)

                oldToNew[curr].neighbors.append(oldToNew[nei])

        return oldToNew[node]
            

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        oldToNew={}

        def dfs(node):

            if node in oldToNew:
                return oldToNew[node]

            copy= Node(node.val)
            oldToNew[node]= copy

            for nei in node.neighbours:
                copy.neighbors.append(dfs(nei))

            return copy
        return dfs(node) if node else None


      







        