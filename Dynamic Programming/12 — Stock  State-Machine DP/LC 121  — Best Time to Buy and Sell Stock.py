class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        

        buy= float("inf")
        profit= float("-inf")


        for element in prices:

            if element < buy:
                buy=element

            if element-buy > profit:
                profit= element

        return profit