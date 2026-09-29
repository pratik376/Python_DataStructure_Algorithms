class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up  # down  # left  # right

        ROWS, COLS= len(board), len(board[0])

        visited=set()

        def dfs (r,c, i):

            if i == len(word):
                return True
            if (
                r < 0 or r >= ROWS
                or c < 0 or c >= COLS
            ):
                return False

            if (r, c) in visited:
                return False

            if board[r][c] != word[i]:
                return False

            visited.add((r,c))
 
            for R,C in directions:

                nr, nc= R +r , C+c

                if nr>= ROWS or nc >= COLS or nr<0 or nc<0 or (nr,nc) in visited:
                    continue

                if dfs( nr,nc, i +1):
                    return True
            visited.remove((r,c))
            return False



        for i in range(ROWS):
            for j in range(COLS):

                if dfs(i,j,0):
                    return True

        return False

        


            
