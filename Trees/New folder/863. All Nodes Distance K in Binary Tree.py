# Definition for a binary tree node.
from typing import List

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
        pass

        