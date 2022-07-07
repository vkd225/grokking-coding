# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

# Use Xor/Bit Manipulation
# Intuition:
# Xor of any two num gives the difference of bit as 1 and same bit as 0.
# Thus, using this we get 1 ^ 1 == 0 because the same numbers have same bits.
# So, we will always get the single element because all the same ones will evaluate to 0 and 0^single_number = single_number.
# Time: O(n)
# Space: O(1)

def single_arrays(nums):
  xor =
  for num in nums:
    xor ^= num
  return xor