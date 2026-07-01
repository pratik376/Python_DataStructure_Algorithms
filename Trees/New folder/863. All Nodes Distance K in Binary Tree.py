# Definition for a binary tree node.
from typing import List
from collections import deque
# find all nodes exactly k steps away from target

# is a big hint for BFS.

# BFS is good when you care about distance in edges.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        parent={}

        def find_parents(node, parent):

            if not node:
                return
            
            parent[node]=parent

            find_parents(node.left)
            find_parents(node.right)
        find_parents(root,None)

        queue=deque()
        queue.append((target,0))

        visted= set()
        visted.add(target)

        answer=[]

        while queue:

            node,distance=queue.popleft()

            if distance==k:
                answer.append(node.val)
            
            if distance>k:
                break

            neighbours= [node.left, node.right, parent[node]]

            for nei in neighbours:

                if nei and nei not in visted:
                    
                    queue.append((nei, distance+1))
                    visted.add(nei)
        
        return answer


        
        


        