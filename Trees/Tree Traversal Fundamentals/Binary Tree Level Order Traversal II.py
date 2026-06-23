# Definition for a binary tree node.
from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:

        
        if not root:
            return []
        
        q=deque()
        answer=[] 

        q.append(root)

        while q:

            qLen= len(q)

            level=[]

            for _ in range(qLen):

                curr= q.popleft()

                if curr:
                    level.append(curr.val)
                    q.append(curr.left)
                    q.append(curr.right)
            
            if level:
             answer.append(level)
        return answer[::-1]            

        
        