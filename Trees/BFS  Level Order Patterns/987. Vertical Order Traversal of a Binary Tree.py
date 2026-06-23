# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from ast import List
from typing import Optional
from collections import defaultdict
from collections import deque


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
        
        q = deque([(root, 0, 0)])

        nodes = [] # column, row, val
        

        while q:

            curr,row,col= q.popleft()
            nodes.append((col,row,curr.val))

            if curr.left:
                q.append((curr.left,row+1, col-1))
            
            if curr.right:
                q.append((curr.right,row+1, col+1))
        
        nodes.sort()

        ans = []
        curr_col = None
        for col, row, val in nodes:
            if col != curr_col:
                ans.append([])
                curr_col = col
            ans[-1].append(val) 
        
        return ans
        