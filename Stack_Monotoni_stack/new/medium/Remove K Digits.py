from collections import deque

def removeKdigit(arr,k):

    stack=deque()

    count=0

    for i in range(len(arr)):

        while stack and arr[i]< stack[-1] and count <k :

            stack.pop()
            count+=1

        stack.append(arr[i])

    while count < k:
        stack.pop()
        count+=1

    result= "".join(stack).lstrip('0')       

    return result if result else '0'              

def removeKdigits(num, k):

    stack = []

    for digit in num:

        while stack and k > 0 and stack[-1] > digit:
            stack.pop()
            k -= 1

        stack.append(digit)

    while k > 0:
        stack.pop()
        k -= 1

    result = "".join(stack).lstrip('0')

    return result if result else "0" 

