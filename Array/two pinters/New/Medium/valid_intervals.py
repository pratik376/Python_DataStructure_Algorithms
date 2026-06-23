from typing import List

def valid_interals (A: List,B : List):

    if len(A)==0 or len(B)==0:
        return []
    
    i=0
    j=0
    result=[]
    while i < len(A) and j < len(B):

        if (A[i][1]>= B[j][0] and A[i][0] <= B[j][1]):

            result.append([max(A[i][0],B[j][0]), min(A[i][1],B[j][1])])

        if A[i][1] < B[j][1]:
           i+=1

        else:
            j+=1

    return result



A=[[0,2],[5,10],[13,23],[24,25]]
B=[]

print(valid_interals(A,B))

