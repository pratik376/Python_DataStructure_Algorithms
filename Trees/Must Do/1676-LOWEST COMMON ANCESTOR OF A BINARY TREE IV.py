from typing import Optional
import math
from collections import defaultdict
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode], nodes: Optional[TreeNode]) -> int:

        target_nodes= set(nodes)
        self.answer= None
        target_count=len(target_nodes)


        def dfs(node):

            if not node:
                return 0
            
            left_sum=dfs(node.left)
            right_sum=dfs(node.right)

            curr_sum= left_sum + right_sum + (1 if node in target_nodes else 0)

            if curr_sum == target_count and self.answer is None:
                self.answer=node
            
            return curr_sum
        dfs(root)
        return self.answer
       


        



            




