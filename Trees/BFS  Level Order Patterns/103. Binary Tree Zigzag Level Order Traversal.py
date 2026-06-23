# Definition for a binary tree node.

from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        answer=[]

        curr_level=-1

        q=deque([root])


        while q:

            curr_level+=1
            curr_node_val=[]
            lenQ=len(q)

            for _ in range(lenQ):

                curr=q.popleft()

                curr_node_val.append(curr.val)

                if curr.left:
                    q.append(curr.left)
                
                if curr.right:
                    q.append(curr.right)
            
            if curr_level %2 !=0:
                curr_node_val=curr_node_val[::-1]
            
            answer.append(curr_node_val)
        return answer
                



               

        