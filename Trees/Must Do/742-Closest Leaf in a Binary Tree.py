from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    def findClosestLeaft(self, root: Optional[TreeNode],k : int) -> int:
        
        parent= {}
        target_node=None

        def find_parents(node):

            if not node:
                return
            if node.val == k:
                target_node=node

            if node.left:
                parent[node.left]=node
            if node.right:
                parent[node.right]=node
            
            find_parents(node.left)
            find_parents(node.right)
        find_parents(root)

        q=deque(target_node)
        visited= set(target_node)
       

        while q:

            curr= q.popleft()

            if not curr.left and not curr.right:
                return curr.val

            if curr.left and curr.left not in visited:
                q.append(curr.left)
                visited.add(curr.left)
            
            if curr.right and curr.right not in visited:
                q.append(curr.right)
                visited.add(curr.right)
            
            if parent[curr] and parent[curr] not in visited:
                q.append(parent[curr])
                visited.add(parent[curr])
        
        return -1






            
        