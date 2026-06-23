





def SlidingWindowMax(arr,k):

    left=0
    right=k-1
    arr_max=[]

    while left < len(arr)-k+1:

        arr_max.append(max(arr[left:right+1]))
        left+=1
        right+=1


    return arr_max    



from collections import deque
def SlidingWindowMax(arr,k):

    result=[]
    queue=deque()

    for right in range(len(arr)):

        while queue and arr[queue[-1]]<arr[right]:
            queue.pop()

        queue.append(right) 

        if queue[0]<= right-k:
            queue.popleft()

        if right>=k-1:
            result.append(arr[queue[0]]) 

    return result           




    

