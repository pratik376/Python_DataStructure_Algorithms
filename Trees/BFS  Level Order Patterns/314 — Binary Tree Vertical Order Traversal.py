from typing import List, Optional

from collections import defaultdict
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def VerticalOder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
        
        q=deque([(root,0)]) # (node,col)
        
        cols= defaultdict(list)
        min_col,max_col=0,0

        while q:

            curr, col = q.popleft()

            min_col,max_col = min(min_col,col), max(max_col,col)

            cols[col].append(curr.val)

            if curr.left:

                q.append((curr.left, col-1))
            
            if curr.right:
                q.append((curr.right, col+1))
        
        return [ cols[c] for c in range(min_col,max_col+1)]




        

