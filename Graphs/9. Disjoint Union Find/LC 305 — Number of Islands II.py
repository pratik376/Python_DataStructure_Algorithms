from typing import List

class Solution:
    def numIslands2( self,m: int,n: int,positions: List[List[int]] ) -> List[int]:

        parents= [i for i in range(m*n)]
        