from typing import List
import heapq
from collections import defaultdict

class Solution:
 def highFive(self, items: List[List[int]]) -> List[List[int]]:
  
  score_dict= defaultdict(list)

  for student in items:
   score_dict[student[0]].append(student[1])
   
  


  

