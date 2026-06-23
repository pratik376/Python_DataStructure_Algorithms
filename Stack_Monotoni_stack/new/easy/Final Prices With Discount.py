from collections import deque

def finalPriceDiscount(arr):

    stack=deque()

    answer= arr.copy()

    for i in range(len(arr)):

        while stack and arr[i] <= arr[stack[-1]]:
            element=  stack.pop()

            answer[element]-=arr[i]

        stack.append(i)

    return answer    