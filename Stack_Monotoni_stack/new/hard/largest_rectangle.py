def largestReact(arr):

    maxArea=0 
    stack=[]   # (index, value)


    for i, val in enumerate(arr):

        start=i

        while stack and stack[-1] > val:

            index, val = stack.pop()

            maxArea= max(maxArea, val * (i-index))

            start=index

        stack.append((start,val))


    for i, h in stack:

        maxArea=max(maxArea, h * (len(arr)-i))

    return maxArea    




