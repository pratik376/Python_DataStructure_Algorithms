def searchRange(arr):

        # this is written by me
        l,r= 0, len(arr)-1
        answer= float('inf')
        while l<=r:

            if arr[l]<arr[r]:
                  return min(answer,arr[l])
                  
            

            mid= (l+r)//2

            answer=min(answer,arr[mid])

            if arr[l] < arr[r]:
                  r=mid-1
            elif arr[l] > arr[r]:
                  l=mid+1
            else:
                  return min(arr[mid],answer)  

        return answer                 


             
# leetcode

def minSearch(arr):
      l,r= 0, len(arr)-1
      answer= float('inf')
      while l<=r:
            
            if arr[l]<= arr[r]:
                  answer=min(answer,arr[l])
                  break

            mid= (l+r) //2

            answer= min(answer,arr[mid])

            if arr[mid]>= arr[l]:
                  l=mid+1
            else:
                  r=mid-1

      return answer                    

arr=[11,13,15,17]
print(searchRange(arr))