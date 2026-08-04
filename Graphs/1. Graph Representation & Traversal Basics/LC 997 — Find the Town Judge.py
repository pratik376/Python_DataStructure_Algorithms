from typing import List
from collections import defaultdict


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        inDegreeCount=defaultdict(int)
        outDegreeCounta=defaultdict(int)

        judge=0
        


        for personA, personB in trust:

            if personA not in visited:
                visited.add(personA)

                edgecount[personB]+=1


        for key in edgecount.keys():

            if edgecount[key] == n-1:
                judge= key

        return judge if judge else -1
        


            

        





        

