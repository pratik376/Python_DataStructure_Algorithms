from typing import Optional

class Node:
    def __init__(self, val: int = None, next: 'Node' = None):
        self.val = val
        self.next = next

class Solution:
    def insert(self, head: Optional['Node'], insertVal: int) -> 'Node':
        if not head:
            new_node = Node(insertVal)
            new_node.next = new_node
            return new_node

        new_node = Node(insertVal)

        # find tail
        tail = head
        while tail.next != head:
            tail = tail.next

        # insert before head
        if insertVal <= head.val:
            new_node.next = head
            tail.next = new_node
            return new_node

        # insert after tail
        if insertVal >= tail.val:
            tail.next = new_node
            new_node.next = head
            return head

        # insert in middle
        curr = head
        while curr.next != head:
            if curr.val <= insertVal <= curr.next.val:
                new_node.next = curr.next
                curr.next = new_node
                return head
            curr = curr.next

        return head