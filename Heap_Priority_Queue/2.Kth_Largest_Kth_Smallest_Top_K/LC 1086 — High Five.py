from typing import List
import heapq
from collections import defaultdict

class Solution:
 def highFive(self, items: List[List[int]]) -> List[List[int]]:
  
  score_dict= defaultdict(list)
  answer=List[List[int]]

  for student in items:
   score_dict[student[0]].append(student[1])

   for key, val in score_dict:

    heapq.heapify_max(val)

    count=5
    sum=0

    while count>0:
     sum+=heapq.heappop_max(val)
     k-=1
    
    answer.append([key, sum/5])

    
     


      





  


  

