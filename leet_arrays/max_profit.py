# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and
# choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


# Input: prices = [7,1,5,3,6,0,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# i =0, compare p[i] with p[i+1] ...
#   if p[i+n] > p[i]:
#     profit = p[i+n] - p[i]
#     maxprofit = max(maxprofit, profit)
#  return maxprofit


def max_profit(prices):
  max_profit = 0
  len_prices = len(prices)

  for i in range(len_prices):
    for j in range(i+1, len_prices):
      if prices[j] > prices[i]:
        curr_profit = prices[j]- prices[i]

        max_profit = max (curr_profit, max_profit)

  return max_profit

profits = [7,1,5,3,6,4]
# print (max_profit(profits))

# sliding window approach
def maxProfit(prices):
  cost = prices[0]
  max_profit = 0

  for i in range(1,len(prices)):
    if(prices[i]<cost):
      cost = prices[i]
    elif(prices[i]>=cost):
      profit = prices[i]-cost
      if(profit>max_profit):
        max_profit = profit
  return max_profit

profits1 = [7,1,5,3,6,0,6]

print (maxProfit(profits1))
