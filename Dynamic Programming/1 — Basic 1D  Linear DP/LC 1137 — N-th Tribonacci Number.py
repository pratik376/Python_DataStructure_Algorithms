class Solution:
    def tribonacci(self, n: int) -> int:

        if n==0:
            return 0

        if n==1 or n==2:
            return 1

        sum_array= [0]* (n+1)
        sum_array[0], sum_array[1], sum_array[2]= 0,1,1

        for i in range(3,n+1):

            sum_array[i]= sum(sum_array[i-3:i])   


        return sum_array[n]         



class Solution:
    def tribonacci(self, n: int) -> int:

        if n==0:
            return 0

        if n==1 or n==2:
            return 1

        a,b,c = 0,1,1
        for i in range(3,n+1):

            current= a +b+c
            a=b
            b=c
            c=current

        return c        



