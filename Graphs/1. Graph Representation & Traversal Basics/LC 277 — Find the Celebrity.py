from typing import List
from collections import defaultdict
# Adjacency matrix
# knows_matrix[a][b] == True means person a knows person b
knows_matrix = [
    [False, True,  True,  False],
    [False, False, True,  False],
    [False, False, False, False],  # Celebrity
    [False, True,  True,  False]
]


def knows(a: int, b: int) -> bool:
    return knows_matrix[a][b]


class Solution:
    def findCelebrity(self, n: int) -> int:

        incomingEdge=defaultdict(int)
        outgoingEdge= defaultdict(int)

        for i in range(len(knows_matrix)):

            for j in range(len(knows_matrix[0])):

                if knows(i,j):

                    incomingEdge[j]+=1
                    outgoingEdge[i]+=1

        for i in range(n):

            if incomingEdge[i] == n-1 and outgoingEdge[i]==0:
                return i

        return -1

class Solution:
    def findCelebrity(self, n: int) -> int:

        candidate=0
#
        for i in range(1,n):

            if knows(candidate, i):
                candidate = i

                # or i can also write this
            
            # if not knows(i, candidate):
            #     candidate= i



        if self.is_celeb(candidate,n):
            return candidate
        else:
            return -1

    def is_celeb(self, candidate, n):

        for i in range(n):

            if i==candidate:
                continue
            else:
                if not knows(i,candidate) or knows(candidate,i):
                    return False
        return True


        



        
        


if __name__ == "__main__":
    sol = Solution()
    print(sol.findCelebrity(4))