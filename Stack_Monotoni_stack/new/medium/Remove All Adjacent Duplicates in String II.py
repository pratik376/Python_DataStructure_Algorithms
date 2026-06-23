from collections import defaultdict

def removeAllDuplicte(str,k):

    stack= []  # count, element

    for ch in str:

        if stack and stack[-1][1]== ch:
            stack[-1][0] +=1
        else:
            stack.append([1, ch])

        if stack[-1][0]==k :
            stack.pop()      

    result=[]

    for ch, count in stack:
        result.append(ch * count)

    return "".join(result)             

