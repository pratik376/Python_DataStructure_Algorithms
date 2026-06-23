# time --> o(n) space --> o(n)

# def sqare_sorted_array(arr):

#     position=len(arr)-1

#     left, right= 0, position

#     answer=[0] * len(arr)

#     while(left <=right):
#         if(abs(arr[left]) > abs(arr[right])):
#             answer[position]= arr[left] **2
#             left+=1
            
#         elif (abs(arr[left])<abs(arr[right])):
#             answer[position]= arr[right] **2
#             right-=1
            

#         else:
#             answer[position]= arr[left] **2
#             left +=1

#         position-=1    

#     return answer

def square_sorted_array(arr):
    n = len(arr)
    left, right = 0, n - 1
    position = n - 1
    answer = [0] * n

    while left <= right:
        if abs(arr[left]) > abs(arr[right]):
            answer[position] = arr[left] ** 2
            left += 1
        else:
            answer[position] = arr[right] ** 2
            right -= 1
        position -= 1

    return answer



nums=[-4,-1,0,3,10]
print(square_sorted_array(nums))



