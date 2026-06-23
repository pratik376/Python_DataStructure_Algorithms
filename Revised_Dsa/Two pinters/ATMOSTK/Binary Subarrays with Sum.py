
def binarySum(arr, goal):



 def atMost(x):

    left=0
    answer=0
    curr_sum=0

    if x < 0: return 0


    for right in range(len(arr)):
      
      curr_sum+=arr[right]

      while curr_sum>x:
        curr_sum-=arr[left]
        left+=1

      answer+= (right-left+1)

    return  answer 
          


 return atMost(goal)- atMost(goal-1)