# Definition for a binary tree node.

from collections import deque
from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []
        
        q=deque([root])

        answer=[]


        while q:

            leval_max=float('-inf')

            for _ in range(len(q)):

                curr= q.popleft()

                leval_max=max(leval_max,curr.val)

                if curr.left:
                    q.append(curr.left)
                
                if curr.right:
                    q.append(curr.right)

            answer.append(leval_max)
        return answer        
        