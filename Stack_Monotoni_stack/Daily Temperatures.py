
def dailyTemparature(arr):

    days=[0]*len(arr)
    stack=[]

    for i in range(len(arr)):

        while stack and arr[i]>arr[stack[-1]]:
            index=stack.pop()
            days[index]= i-index

        stack.append(i)  

    return days



s = [70, 71, 70, 72, 69, 74]
print(dailyTemparature(s))