from typing import List
from collections import defaultdict


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        inDegreeCount=defaultdict(int)
        outDegreeCount=defaultdict(int)

        judge=0
        


        for personA, personB in trust:

            inDegreeCount[personB]+=1
            outDegreeCount[personA]+=1
        


        return judge if judge else -1
        


            

        





        

