# Definition for a binary tree node.
from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        parents= {root: None}

        que=deque([root])

        while p not in parents or q not in parents:

            node= que.popleft()

            if node.left:
                parents[node.left]=node
                que.append(node.left)

            if node.right:
                parents[node.right]= node
                que.append(node.right)

        ancestor=set()

        while p:
            ancestor.add(p)
            p= parents[p]

        while q not in ancestor:
            q= parents[q]

        return q                    


        