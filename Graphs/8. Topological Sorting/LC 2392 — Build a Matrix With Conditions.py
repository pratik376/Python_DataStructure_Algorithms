from typing import List


class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:


        def dfs():
            pass

        def topo_sort(edges):
            pass


        row_order= topo_sort()
        column_order= topo_sort()

        answer= [[0]*k for _ in range(k)]

        if not row_order or not column_order:
            return []


        rows_set= {n:i for i,n in enumerate(row_order)}
        columns_set= {n:i for i,n in enumerate(column_order)}

        for num in range(1, k+1):
            r,c = rows_set[num], columns_set[num]
            

            
        