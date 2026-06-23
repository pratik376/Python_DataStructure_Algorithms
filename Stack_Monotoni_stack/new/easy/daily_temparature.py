from collections import deque

def dailyTemp(arr):

    n= len(arr)

    result=[0] *n 

    stack= deque()


    for i in range(len(arr)):

        while stack and arr[i]> arr[stack[-1]]:

            index= stack.pop()

            result[index]= i-index

        stack.append(i)

    return result    

