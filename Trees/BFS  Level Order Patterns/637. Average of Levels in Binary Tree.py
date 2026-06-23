# Definition for a binary tree node.
from typing import List, Optional

from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        if not root:
            return []

        answer=[]
        q=deque([root])

        while q:

            total_element=len(q)
            sum=0

            for _ in range(total_element):

                node= q.popleft()

                sum+= node.val

                if node.left:

                    q.append(node.left)
                

                if node.right:
                    q.append(node.right)
            
            avg=sum/total_element
            answer.append(avg)
        return answer
        






        

        
        