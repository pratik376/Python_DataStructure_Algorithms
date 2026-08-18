from typing import List


class Solution:
    def countServers(self, heights: List[List[int]]) -> int:

        ROWS, COLS= len(heights), len(heights[0])
        
        row_cnt= [0] * ROWS
        col_cnt= [0] * COLS
        
        for i in range(ROWS):
            for j in range(COLS):

                if heights[i][j]==1:

                    row_cnt[i]+=1
                    col_cnt[j]+=1

        result=0
#dgddgf
        for i in range(ROWS):
            for j in range(COLS):

                if heights[i][j]==1:

                    if row_cnt[i] >1 or col_cnt[j]>1:
                        result+=1

        return result
        