#You are given an array prices where prices[i] is the price of a given stock on the ith day 
#You want to maximize your profit by choosing a single day to buy one stock and choosing 
#A different day in the future to sell that stock 
#Return the maximum profit you can achieve from this transaction
#if you cannot achieve any profit return 0
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #we can use a sliding window algorithm to accomplish this 
        #tracking the highest profit as we go along the prices
        #if nothing is positive then we will return 0 i.e only update 'profit' when positive
        profit, buy_price, sell_price = 0, 0, 0
        while sell_price < len(prices):
            difference = -(prices[buy_price] - prices[sell_price])
            if difference > profit:
                profit = difference
            if difference < 0:
                buy_price = sell_price
            sell_price += 1
        return profit
