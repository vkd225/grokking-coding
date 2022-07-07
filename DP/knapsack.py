# Items: { Apple, Orange, Banana, Melon }
# Weights: { 2, 3, 1, 4 }
# Profits: { 4, 5, 3, 7 }
# Knapsack capacity: 5

# Let's try to put various combinations of fruits in the knapsack, such that their total weight is not more than 5:

# Apple + Orange (total weight 5) => 9 profit
# Apple + Banana (total weight 3) => 7 profit
# Orange + Banana (total weight 4) => 8 profit
# Banana + Melon (total weight 5) => 10 profit

# This shows that Banana + Melon is the best combination as it gives us the maximum profit,
# and the total weight does not exceed the capacity.


# Given two integer arrays to represent weights and profits of N items,
# we need to find a subset of these items which will give us maximum profit such
# that their cumulative weight is not more than a given number C.
# Each item can only be selected once, which means either we put an item in the knapsack or we skip it.

def solve_knapsack(profits, weights, capacity):
  currIdx = 0
  # create a 2d array for dp
  dp = [-1 for i in range(capacity + 1) for j in range(len(profits))]
  return knapsack_recursive(profits, weights, capacity, currIdx)


def knapsack_recursive(profits, weights, capacity, currIdx):
  # base check
  if capacity <= 0 or currIdx >= len(profits):
    return 0

  if dp[currIdx][profits] != -1:
    return dp[currIdx][capacity]

  # recursive call after choosing the element at the currentIndex
  # if the weight of the element at currentIndex exceeds the capacity, we  shouldn't process this
  profit1 = 0
  if weights[currIdx] <= capacity:
    profit1 = profits[currIdx] + knapsack_recursive(profits, weights, capacity - weights[currIdx], currIdx + 1)


  # recursive call after excluding the element at the currentIndex
  profit2 = knapsack_recursive(profits, weights, capacity, currIdx + 1)

  dp[currIdx][capacity] = max(profit1, profit2)
  return dp[currIdx][capacity]

def main():
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))


main()