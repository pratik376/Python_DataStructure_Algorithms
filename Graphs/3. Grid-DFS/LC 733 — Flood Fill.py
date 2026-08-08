from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        ROWS, COLUMS= len(image), len(image[0])

        original_color= image[sr][sc]


        def coloring(r,c):

            if (r< 0 or c <0 or r==ROWS  or c==COLUMS or image[r][c] != original_color or image[r][c]==color):
                return

            if image[r][c] == original_color:
                image[r][c]= color

                coloring(r,c+1)
                coloring(r,c-1)
                coloring(r+1,c)
                coloring(r-1,c)

        coloring(sr,sc)
        return image

        

    
        