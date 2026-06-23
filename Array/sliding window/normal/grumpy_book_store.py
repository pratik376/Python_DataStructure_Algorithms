from typing import List
def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
  
     

     window, max_window=0,0

     satisfied=0

     for i in range(minutes):
          
          if grumpy[i]:
               window+=customers[i]
          else:
               satisfied+=customers[i]

     max_window=window          

     for j in range(minutes,len(customers)):

          if grumpy[j]:
               window+=customers[j]

          else:
               satisfied+= customers[j]

          if grumpy[j-minutes]:
               window-= customers[j-minutes]

          max_window=max(max_window,window)

     return satisfied+ max_window           


# 2nd approach


def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
     l=0
     window, max_window= 0,0

     statisfied= 0

     for r in range(len(customers)):
          if grumpy[r]:
               window+=customers[r]
          else:
               statisfied+= customers[r] 

          if r - l + 1 > minutes:
               if grumpy[l]:
                 window-= customers[l]
               l+=1 
          max_window= max(window, max_window)  

     return statisfied + max_window          
                                          


                               


