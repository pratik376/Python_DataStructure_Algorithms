# Definition for a binary tree node.
from typing import Optional


# height
# depth
# diameter
# longest path
# maximum path
# balanced
# subtree
# path through node

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:


       self.max_path=0

       def dfs(node):
           
           if not node:
               return 0
           
           left_len= dfs(root.left)
           right_len=dfs(root.right)

           left_path=0
           right_path=0

           if node.left and node.left.val== node.val:
               left_path=left_len+1
           if node.right and node.right.val== node.val:
               right_path= right_len+1
            
           self.max_path= max(self.max_path, left_path+ right_path)

           return max(left_len,right_len)
    
       dfs(root)
       return self.max_path


        