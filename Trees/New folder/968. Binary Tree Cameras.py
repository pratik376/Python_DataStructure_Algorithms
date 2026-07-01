# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# If child needs camera:
#     Put camera at current node
#     Return "I have camera"

# Else if child has camera:
#     Current node is covered
#     Return "I am covered"

# Else:
#     Children are covered, but current node is not covered
#     Return "I need camera"

# 0 = node needs camera
# 1 = node has camera
# 2 = node is covered or it does not need camera

class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:

        self.camera= 0

        def dfs(node):

            if not node:
                return 2  # covered
            
            left= dfs(node.left)
            right=dfs(node.right)


            # If any child needs camera, put camera here
            if left==0 or right==0:
                self.camera+=1
                return 1 # I have camera
            
            if left==1 or right==1:
                return 2 # covered
            
            # Otherwise, this node is not covered
            return 0  # needs camera
        if dfs(root) == 0:
            self.camera+=1

        return self.camera
            

        