from collections import deque

def NextGraterElement(arr):

    n=len(arr)
    stack= deque()
    arr=arr+arr

    results=[-1] * n


    for i in range(len(arr)):

        while stack and arr[i] > arr[stack[-1]]:

            index= stack.pop()

            if index < n:
             results[index]= arr[i]
            if i < n:  # optional
              stack.append(i)

    return results    

from collections import deque

def nextGreaterElement(arr):
    n = len(arr)
    stack = deque()  # store indices
    result = [-1] * n

    for i in range(2 * n):  # simulate two passes
        current = arr[i % n]
        while stack and current > arr[stack[-1]]:
            index = stack.pop()
            result[index] = current
        if i < n:  # only push original indices
            stack.append(i)

    return result