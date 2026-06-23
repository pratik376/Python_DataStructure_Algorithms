def people(arr):

    N=len(arr)

    res=[0] * N

    stack=[]

    for i in range(N-1,-1,-1):

        hei= arr[i]

        visible=0

        while stack and hei > stack[-1]:
            visible+=1
            stack.pop()

        if stack:
            visible+=1

        res[i]=visible
        stack.append(hei)

    return res            