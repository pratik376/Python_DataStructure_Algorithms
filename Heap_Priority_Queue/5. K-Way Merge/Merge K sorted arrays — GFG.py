import heapq
class Solution:
    def mergeArrays(self, mat):

        heap=[]
        answer=[]

        for i in range(len(mat)):

            heapq.heappush(heap, (mat[i][0],i,0))  # (element, array_index, position_of_element)

        while heap:

            element, array_index, position_of_element= heapq.heappop(heap)

            answer.append(element)

            if position_of_element + 1 < len(mat[array_index]):
                heapq.heappush(heap, (mat[array_index][position_of_element + 1],array_index,position_of_element + 1))
        
        return answer






        
        