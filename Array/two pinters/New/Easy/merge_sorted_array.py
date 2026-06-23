#nums1=[1,2,3,0,0,0], m=3; nums2=[2,5,6], n=3 → [1,2,2,3,5,6]
# Time: O(m+n) Space: O(1) 


# def merged_sorted_array(num1,m,num2,n):

#     position= m+n-1
#     m=m-1
#     n=n-1

#     while(m !=-1 and n!=-1):

#         if(num1[m]> num2[n]):
#             num1[position]=num1[m]
#             m-=1
#         else:
#             num1[position]= num2[n]
#             n-=1
#         position-=1

#     while(m!=-1):
#         num1[position]=num1[m]
#         position-=1
#         m-=1  

#     while(n!=-1):
#         num1[position]=num2[n]
#         position-=1
#         n-=1        

#     return num1

def merged_sorted_array(num1, m, num2, n):
    position = m + n - 1
    m -= 1
    n -= 1

    while m >= 0 and n >= 0:
        if num1[m] > num2[n]:
            num1[position] = num1[m]
            m -= 1
        else:
            num1[position] = num2[n]
            n -= 1
        position -= 1

    # Only need to copy remaining elements from num2
    while n >= 0:
        num1[position] = num2[n]
        n -= 1
        position -= 1

    return num1


nums1=[1,3,7,0,0,0]
m=3
nums2=[2,5,6]
n=3

print(merged_sorted_array(nums1,m,nums2,n))





