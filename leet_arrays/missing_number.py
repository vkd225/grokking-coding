# Given an array nums containing n distinct numbers in the range [0, n],
# return the only number in the range that is missing from the array.


# Input: nums = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3].
# 2 is the missing number in the range since it does not appear in nums.


def missing_number(nums):
  nums.sort()

  for i in range(len(nums)):
    if nums[i] != i:
      return i
    if i == len(nums) -1:
      return len(nums)

  return None

nums = [3,0,1]
print (missing_number(nums))


# pretty good solution
def missingNumber(nums):
  n = len(nums)
  # The formula to find the sum of n nunbers from 0 is n*(n+1)/2.
  # if subtract the sum of n numbers and the nums given,
  # we will find the missing number between them.
  #  // is floor division
  return n * (n+1) // 2 - sum(nums)


