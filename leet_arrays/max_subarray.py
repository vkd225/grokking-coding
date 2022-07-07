# Given an integer array nums, find the contiguous subarray
# (containing at least one number) which has the largest sum and return its sum.

# A subarray is a contiguous part of an array.

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.





# max_sum = nums[i]
# i = 0
# j = 1

# while  j < len(nums):
#   curr_max = max_sum + nums[j]
#   if curr_max > max_sum:
#     j += 1
      # max_sum = curr_max
#    else:
#     i += 1

# [-2,1,-3,4,-1,2,1,-5,4]
# [-2,1,-3, 4]



def max_subarray(nums):
  i = 0
  j = 1
  max_sum = nums[i]
  curr_sum = nums[i]

  while  i < len(nums):
    prev_sum = curr_sum
    curr_sum = prev_sum + nums[j]

    if curr_sum > max_sum:
      max_sum = curr_sum
      j += 1
    else:
      curr_sum = max_sum + nums[i]
      i += 1
  return max_sum

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(max_subarray(nums))


def maxSubArray(self, nums: List[int]) -> int:
  maxSum = nums[0] # Keep track of max sub-array sum
  curSum = 0 # Keep track of current sub-array sum

  for num in nums:
    if curSum + num < num:
      curSum = num # Start a new sub-array
    else:
      curSum = curSum + num # Extend from our previous sub-array
    maxSum = max(maxSum, curSum)
  return maxSum





