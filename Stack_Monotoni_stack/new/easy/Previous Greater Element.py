from collections import deque


def previousGraterElement(arr):

    answer= [-1] * len(arr)

    stack= deque()

    for i in range(len(arr)):

        while stack and arr[i]>= arr[stack[-1]]:

             stack.pop()

        if stack:

            answer[i]= arr[stack[-1]]

        stack.append(i)           


    return answer        


arr= [10, 4, 2, 20, 40, 12, 30]
print(previousGraterElement(arr))