class Solution(object):
    def maxProfit(self, prices):
        '''#lets write the previous code first 
        prev_profit =0 # tracks the highest profit
        profit = 0

        min_for_now =0
        current = 0

        for current in prices :
            if current < min_for_now:
                min_for_now = current
            profit = current - min_for_now

            if profit > prev_porfit and (profit and prev_porfit >0):
                prev_profit = profit '''

        #this is the previous code which allows only one byuy and sell, one profit, 
        # now we will allow multiple buys and sell, 

        #after sell buy the next stock immidiatelu , greedy approach, 

        # plan, first step is same as the previous algo, for this one, after sell, set min_for_now to the stock immidiately, sold, append profits to array, add them up and then return

        profit = 0 
        positive_profits = []
        min_for_now=prices[0]
        current = 0
        total_profit = 0

        for current in prices  :
            if current < min_for_now :
                min_for_now = current

            profit = current - min_for_now
            if profit > 0:
                positive_profits.append(profit)
                min_for_now = current

        for i in positive_profits:
            total_profit = total_profit + i
        return total_profit
        



        