# Definition for a binary tree node.
from typing import List, Optional

from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []


        q=deque([root])
        answer=[]

        while q:

            qLen=len(q)

            for i in range(qLen):

                curr=q.popleft()

                if i == qLen-1:
                    answer.append(curr.val)
                
                if curr.left:
                    q.append(curr.left)
                
                if curr.right:
                    q.append(curr.right)
        return answer

# recursive



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        answer=[]

        def dfs (root, level):

            if not root:
                return
            
            if level== len(answer):
                answer.append(root.val)
            
            dfs(root.right, level+1)
            dfs(root.left, level+1)

        dfs(root,0)
        return answer
