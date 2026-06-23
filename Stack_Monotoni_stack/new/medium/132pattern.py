def _132Pattern(arr):

    stack= [ ] # [value, min_value]
    currentMin=arr[0]


    for k in arr[1:]:

        while stack and k>=stack[-1][0]:
            stack.pop()

        if stack and k > stack[-1][1]: 
            return True
        
        stack.append([k,currentMin])
        currentMin=min(currentMin,k)

    return False        





