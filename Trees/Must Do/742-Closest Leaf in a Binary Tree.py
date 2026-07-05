from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findClosestLeaf(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1

        parent = {root: None}
        target_node = None

        def find_parents(node):
            nonlocal target_node
            if not node:
                return

            if node.val == k:
                target_node = node

            if node.left:
                parent[node.left] = node
                find_parents(node.left)

            if node.right:
                parent[node.right] = node
                find_parents(node.right)

        find_parents(root)

        if not target_node:
            return -1

        q = deque([target_node])
        visited = {target_node}

        while q:
            curr = q.popleft()

            if not curr.left and not curr.right:
                return curr.val

            for guest in (curr.left, curr.right, parent[curr]):
                if guest and guest not in visited:
                    visited.add(guest)
                    q.append(guest)

        return -1