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

        def find_parents(node):

            if not node:
                return
            
            if node.left:
                parent[node.left]=node
            if node.right:
                parent[node.right]=node
        find_parents(root)

        q=deque(())


            
        