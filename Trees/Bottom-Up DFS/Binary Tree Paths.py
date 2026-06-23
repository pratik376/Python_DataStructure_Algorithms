# Definition for a binary tree node.
from typing import List, Optional

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        if not root:
            return []
        
        
        q= deque([(root,[root.val])]) # (node, path) 
        # q= deque([root,[root.val]]) # this is only list [root, root.val] not a tuple like this (node,path)


        answer=[]


        while q:
            
                node, path= q.popleft()

                if not node.left and not node.right:
                    
                    
                    answer.append('->'.join(map(str,path)))

                if node.left:

                    q.append([node.left, path+[node.left.val]])
                
                if node.right:
                    q.append([node.right, path+ [node.right.val]])
        return answer