# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

stairs_dp = {}
def climb_stairs(n):

  if n == 1:
    return 1

  if n == 2:
   return 2

  if n in stairs_dp:
    return stairs_dp.get(n)

  stairs_dp[n] = climb_stairs(n-1) + climb_stairs(n-2)

  return stairs_dp[n]

print (climb_stairs(4))
