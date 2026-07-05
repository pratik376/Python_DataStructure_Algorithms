class TreeAncestor:

    def __init__(self, n: int, parent: list[int]):
        self.LOG = (n).bit_length()
        self.up = [[-1] * self.LOG for _ in range(n)]

        # 1st ancestor
        for node in range(n):
            self.up[node][0] = parent[node]

        # 2^j-th ancestors
        for j in range(1, self.LOG):
            for node in range(n):
                prev = self.up[node][j - 1]
                if prev != -1:
                    self.up[node][j] = self.up[prev][j - 1]

    def getKthAncestor(self, node: int, k: int) -> int:
        bit = 0
        while k > 0 and node != -1:
            if k & 1:
                node = self.up[node][bit]
            k >>= 1
            bit += 1
        return node