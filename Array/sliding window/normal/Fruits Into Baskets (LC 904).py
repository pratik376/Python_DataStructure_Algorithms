from typing import List
from collections import defaultdict

def totalFruit(self, fruits: List[int]) -> int:
    left=0
    frequency= defaultdict(int)
    res=0


    for right in range(len(fruits)):

        frequency[fruits[right]]+=1

        while len(frequency)>2:

            frequency[fruits[left]]-=1

            if not frequency[fruits[left]]:
                frequency.pop(fruits[left])

            left+=1

        res= max(res, right-left+1) 

    return res           

