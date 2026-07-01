# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# this is the solution class
class Solution:
    def LongestZigZag(self, root: Optional[TreeNode]) -> int:

        self.answer=0
        
        def dfs(node, left_zig, right_zig):

            if not node:
                return 
            
            self.answer= max(self.answer, left_zig,right_zig)

    
            dfs(node.right, 0, left_zig+1)
            dfs(node.left, right_zig+1, 0)
           
        
        dfs(root, 0,0)
        
        return self.answer