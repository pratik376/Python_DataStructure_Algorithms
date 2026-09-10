from collections import deque

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
