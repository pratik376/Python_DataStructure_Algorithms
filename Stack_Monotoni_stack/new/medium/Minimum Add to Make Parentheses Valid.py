def minimumToAdd(arr):
    
    stack=[]
    for ch in arr:

        if stack and ch==')' and stack[-1]=='(':
            stack.pop()
            continue
        stack.append(ch)    

    return len(stack)    


def minimumToAdd(arr):
    
    open_brac= 0
    close_brac=0
    for ch in arr:

        if ch=='(':
            open_brac+=1

        if ch==')': 
          if open_brac != 0:
            open_brac-=1
          else:
            close_brac+=1

    return open_brac + close_brac            


        




