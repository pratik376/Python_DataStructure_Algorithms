from typing import List
from collections import defaultdict

# time and space complexity it  O(V+E) and O(v) 

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        inDegreeCount=defaultdict(int)
        outDegreeCount=defaultdict(int)

        judge=0

        for personA, personB in trust:

            inDegreeCount[personB]+=1
            outDegreeCount[personA]+=1

        for i in range(1, n+1):

            if inDegreeCount[i]== n-1 and outDegreeCount[i]==0:
                return i
        
        return judge if judge else -1
        


            

        





        

