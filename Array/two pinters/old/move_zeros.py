
num=[0,1,0,3,12]

def swap(num,i,j):
 temp=num[i]
 num[i]=num[j]
 num[j]=temp

def moveZeros(num):

  i=0
  j=0
  n=len(num)

  while(j<n):
  
   if num[j]!=0:
    swap(num,i,j)
    i+=1
   else:
    j+=1

moveZeros(num)
print(num)