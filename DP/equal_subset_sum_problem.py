# Given a set of positive numbers,
# find if we can partition it into two subsets such that the sum of elements in both subsets is equal.


# Input: {1, 2, 3, 4}
# Output: True
# Explanation: The given set can be partitioned into two subsets with equal sum: {1, 4} & {2, 3}

# Input: {2, 3, 4, 6}
# Output: False
# Explanation: The given set cannot be partitioned into two subsets with equal sum.


def can_partition(inp):
  sum_inp = sum(inp)
  n = len(inp)

  if sum_inp % 2 != 0 or n == 0:
    return False

  curr_idx = 0
  return recursive_sum(inp, sum_inp/2, 0)


def recursive_sum(inp, s, curr_idx):
  if s == 0:
    return True

  if curr_idx >= len(inp):
    return False

  if inp[curr_idx] <= s:
    if (recursive_sum(inp, s - inp[curr_idx], curr_idx + 1)):
      return True

  return recursive_sum(inp, s, curr_idx + 1)

def main():
  print("Can partition1: " + str(can_partition([1, 2, 3, 4])))
  print("Can partition1: " + str(can_partition([1, 1, 3, 4, 7])))
  print("Can partition1: " + str(can_partition([2, 3, 4, 6])))


main()




def can_partition(num):
  s = sum(num)

  # if 's' is a an odd number, we can't have two subsets with equal sum
  if s % 2 != 0:
    return False

  # initialize the 'dp' array, -1 for default, 1 for true and 0 for false
  dp = [[-1 for x in range(int(s/2)+1)] for y in range(len(num))]
  return True if can_partition_recursive(dp, num, int(s / 2), 0) == 1 else False


def can_partition_recursive(dp, num, sum, currentIndex):
  # base check
  if sum == 0:
    return 1

  n = len(num)
  if n == 0 or currentIndex >= n:
    return 0

  # if we have not already processed a similar problem
  if dp[currentIndex][sum] == -1:
    # recursive call after choosing the number at the currentIndex
    # if the number at currentIndex exceeds the sum, we shouldn't process this
    if num[currentIndex] <= sum:
      if can_partition_recursive(dp, num, sum - num[currentIndex], currentIndex + 1) == 1:
        dp[currentIndex][sum] = 1
        return 1

    # recursive call after excluding the number at the currentIndex
    dp[currentIndex][sum] = can_partition_recursive(
      dp, num, sum, currentIndex + 1)

  return dp[currentIndex][sum]


def maindp():
  print("Can partition: " + str(can_partition([1, 2, 3, 4])))
  print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
  print("Can partition: " + str(can_partition([2, 3, 4, 6])))


maindp()