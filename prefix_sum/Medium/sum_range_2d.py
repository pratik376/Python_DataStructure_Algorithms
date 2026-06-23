class RangeSumQuery2D:
    def __init__(self, matrix):
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            self.prefix = []
            return

        m = len(matrix)
        n = len(matrix[0])
        self.prefix = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                top = self.prefix[i - 1][j] if i > 0 else 0
                left = self.prefix[i][j - 1] if j > 0 else 0
                top_left = self.prefix[i - 1][j - 1] if i > 0 and j > 0 else 0
                self.prefix[i][j] = matrix[i][j] + top + left - top_left

    def sumRegion(self, row1, col1, row2, col2):
        total = self.prefix[row2][col2]
        top = self.prefix[row1 - 1][col2] if row1 > 0 else 0
        left = self.prefix[row2][col1 - 1] if col1 > 0 else 0
        top_left = self.prefix[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0
        return total - top - left + top_left
