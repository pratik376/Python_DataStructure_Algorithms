def duplicate(arr):
     fast= arr[0]
     slow= arr[0]

     while True:
          slow=arr[slow]
          fast= arr[arr[fast]]
          
          if fast == slow:
               break

     slow=arr[0]

     while fast != slow:

          slow=arr[slow]
          fast=arr[fast]

     return slow  

               