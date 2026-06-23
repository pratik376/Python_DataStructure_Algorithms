from collections import deque

def NextGraterElement(arr):

    n=len(arr)
    stack= deque()

    results=[-1] * n


    for i in range(len(arr)):

        while stack and arr[i] > arr[stack[-1]]:

            index= stack.pop()

            results[index]= arr[i]

        stack.append(i)

    return results    



