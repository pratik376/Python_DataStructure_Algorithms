from typing import Optional
from collections import deque, defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    def findClosestLeaf(self, root: Optional[TreeNode],k : int) -> int:
        
        parent=defaultdict(TreeNode)
        self.target_node=None

        def find_parents(node):

            if not node:
                return
            if node.val == k:
                self.target_node=node

            if node.left:
                parent[node.left]=node
            if node.right:
                parent[node.right]=node
            
            find_parents(node.left)
            find_parents(node.right)
        find_parents(root)

        target_node=self.target_node

        q=deque([target_node])
        visited= set(target_node)
       

        while q:

            curr= q.popleft()

            if not curr.left and not curr.right:
                return curr.val


            guests=[curr.left , curr.right, parent[curr]]

            for guest in guests:

                if guest and guest not in visited:
                    q.append(guest)
                    visited.add(guest)

           

            # if curr.left and curr.left not in visited:
            #     q.append(curr.left)
            #     visited.add(curr.left)
            
            # if curr.right and curr.right not in visited:
            #     q.append(curr.right)
            #     visited.add(curr.right)
            
            # if parent[curr] and parent[curr] not in visited:
            #     q.append(parent[curr])
            #     visited.add(parent[curr])
        
      






            
        