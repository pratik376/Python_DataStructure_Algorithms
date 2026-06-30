# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right




class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:


        self.max_sum=float('-inf')


        def dfs(node):

            if not node:
                return 0
            
            left_sum=max(0,dfs(node.left))
            right_sum=max(0,dfs(node.right))

            total_sum= left_sum+ right_sum+ node.val

            self.max_sum= max(self.max_sum, total_sum)
        
            return node.val + max(left_sum,right_sum)
        dfs(root)
        return self.max_sum


        