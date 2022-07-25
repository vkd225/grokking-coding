# Given a value V, if we want to make a change for V cents,
# and we have an infinite supply of each of C = { C1, C2, .., Cm} valued coins,
# what is the minimum number of coins to make the change?
# If it's not possible to make a change, print -1.

# Input: coins[] = {25, 10, 5}, V = 30
# Output: Minimum 2 coins required We can use one coin of 25 cents and one of 5 cents

# Input: coins[] = {9, 6, 5, 1}, V = 11
# Output: Minimum 2 coins required We can use one coin of 6 cents and 1 coin of 5 cents

def min_coin(coins, v):
  len_coins = len(coins)
  return min_coin_problem(coins, v, len_coins)

def min_coin_problem(coins, V, m):
  if (V == 0):
    return 0

    # Initialize result
    res = float("inf")

    # Try every coin that has smaller value than V
    for i in range(0, m):
      if (coins[i] <= V):
        sub_res = min_coin_problem(coins, V-coins[i], m)

        # Check for INT_MAX to avoid overflow and see if
        # result can minimized
        if (sub_res != float("inf") and sub_res + 1 < res):
          res = sub_res + 1

    return res

# Driver program to test above function
coins = [9, 6, 5, 1]
m = len(coins)
V = 11
# print("Minimum coins required is",min_coins(coins, V))


coins.sort() # c = [1, 5, 6, 9]

# Bottom up approach
def get_min_coins_dp(coins, V):
  dp = [float("inf") for amount in range(V + 1)]

  dp[0] = 0

  for c in coins:
    for amount, min_coin in enumerate(dp):
      if c <= amount:
        dp[amount] = min(min_coin, 1 + dp[amount - c])

  print (dp)
  return dp[V]

print(get_min_coins_dp(coins, V))


