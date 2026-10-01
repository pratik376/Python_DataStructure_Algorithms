class Solution:
    def totalNQueens(self, n: int) -> int:



        columns= set()
        positiveDiagonal= set()
        negativeDiagonal=set()
        borard=  [['.'] for i in range(n)]
        count=0

        def backtrack (r):
            nonlocal count

            if r==n:

                count+=1
                return

            for c in range(n):

                if c in columns or (r+c) in positiveDiagonal or (r-c) in negativeDiagonal:
                    continue

                columns.add(c)
                positiveDiagonal.add(r+c)
                negativeDiagonal.add(r-c)

                borard[r][c]='Q'

                columns.remove(c)
                positiveDiagonal.remove(r+c)
                negativeDiagonal.remove(r-c)

            backtrack(0)
            return count





        