from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        stack = []
        curr = root
        prev = None
        first = second = None

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()

            if prev and prev.val > curr.val:
                if first is None:
                    first = prev
                second = curr

            prev = curr
            curr = curr.right

        first.val, second.val = second.val, first.val

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        first = second = prev = None
        curr = root

        while curr:
            if not curr.left:
                if prev and prev.val > curr.val:
                    if first is None:
                        first = prev
                    second = curr
                prev = curr
                curr = curr.right
            else:
                pred = curr.left
                while pred.right and pred.right != curr:
                    pred = pred.right

                if not pred.right:
                    pred.right = curr
                    curr = curr.left
                else:
                    pred.right = None

                    if prev and prev.val > curr.val:
                        if first is None:
                            first = prev
                        second = curr

                    prev = curr
                    curr = curr.right

        first.val, second.val = second.val, first.val