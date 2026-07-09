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
     count-=1
    
    answer.append([key, sum/5])

    return answer

from typing import List
import heapq
from collections import defaultdict

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        score_dict = defaultdict(list)

        for student_id, score in items:
            heapq.heappush(score_dict[student_id], score)
            if len(score_dict[student_id]) > 5:
                heapq.heappop(score_dict[student_id])

        answer = []

        for student_id in sorted(score_dict.keys()):
            avg = sum(score_dict[student_id]) // 5
            answer.append([student_id, avg])

        return answer
     


      





  


  

