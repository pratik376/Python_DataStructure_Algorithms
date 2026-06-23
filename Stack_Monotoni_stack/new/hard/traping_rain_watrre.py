from collections import deque

def trapingRainWater(arr):

    water= 0 

    stack= deque()


    for  i in range(len(arr)):

        while stack and arr[i] > arr[stack[-1]]:

            current= stack.pop()

            if not stack:
                break
            
            width= i- stack[-1] -1

            height= min(arr[stack[-1]], arr[i] ) - arr[current]

            water+= width * height

        stack.append(i) 

    return water       

