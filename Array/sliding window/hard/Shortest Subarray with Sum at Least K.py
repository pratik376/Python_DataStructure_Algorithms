from collections import deque

def subarrayWithSumAtLeasK(arr,k):

    left=0
    answer=float('inf')
    current_sum=0
    


    for right in range(len(arr)):

        current_sum+=arr[right]


        while current_sum>= k:

            answer=min(answer,right-left+1)

            if arr[left]> 0:
             current_sum-=arr[left]
            else:
                current_sum+=-arr[left]
            left +=1

    return answer if answer!= float('inf') else -1        


# liding window only works if: Removing elements always decreases sum
# Yes—classic sliding window (two pointers) works only when all numbers are non-negative.
    

def subarrayWithSumAtLeasK(arr,k):

    res=float('inf')
    q=deque()
    current_sum=0

    for r in range(len(arr)):
        
        current_sum += arr[r]

        if current_sum >= k:

            res= min(res, r+1)


        while q and  current_sum- q[0][0] >=k:
            
            element, index= q.popleft()
            res=min(res, r-index)

        while q and q[-1][0] >= current_sum : 
            q.pop()  
        q.append((current_sum,r))

    return -1 if res==float('inf') else res        


    



