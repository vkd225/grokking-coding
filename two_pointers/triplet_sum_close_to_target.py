# Given an array of unsorted numbers and a target number, find a triplet in the array whose
# sum is as close to the target number as possible, return the sum of the triplet.
# If there are more than one such triplet, return the sum of the triplet
# with the smallest sum.

# Input: [-2, 0, 1, 2], target=2
# Output: 1
# Explanation: The triplet [-2, 1, 2] has the closest sum to the target.

# Input: [1, 0, 1, 1], target=100
# Output: 3
# Explanation: The triplet [1, 1, 1] has the closest sum to the target.

if abs(target_diff) < abs(smallest_difference) or
(abs(target_diff) == abs(smallest_difference) and
target_diff > smallest_difference):



def triplet_close_to_sum(arr, target):

  if len(arr) < 3:
    return "No triplets"


  if len(arr) == 3:
    for i in range(len(arr)):
      min_sum_triplets += arr[i]
    return min_sum_triplets

  arr.sort()

  min_sum_triplets = float("inf")

  for i in range(len(arr)):
    two_sum(arr, arr[i], i+1, min_sum_triplets, target)

  return min_sum_triplets


def two_sum(arr, start_e, start, min_sum_triplets, target):
  target_sum = target - start_e
  end = len(arr) - 1

  while (start < end):
    current_sum = arr[start] + arr[end]
    if current_sum == target_sum:
      min_sum_triplets = 0
      return min_sum_triplets
    elif target_sum > current_sum:
        end -= 1
        min_sum_triplets = min (min_sum_triplets, target - (current_sum + start_e))
    else:

      start += 1
      min_sum_triplets = min (min_sum_triplets, target - (current_sum + start_e))

  return min_sum_triplets

arr = [-2, 0, 1, 2]
target=2

print (triplet_close_to_sum(arr, target))



import math
def triplet_sum_close_to_target(arr, target_sum):
  arr.sort()
  smallest_difference = math.inf
  for i in range(len(arr)-2):
    left = i + 1
    right = len(arr) - 1
    while (left < right):
      target_diff = target_sum - arr[i] - arr[left] - arr[right]
      if target_diff == 0:  # we've found a triplet with an exact sum
        return target_sum  # return sum of all the numbers

      # the second part of the following 'if' is to handle the smallest sum
      # when we have more than one solution
      if abs(target_diff) < abs(smallest_difference) or
        (abs(target_diff) == abs(smallest_difference) and
        target_diff > smallest_difference):
        smallest_difference = target_diff  # save the closest and the biggest difference

      if target_diff > 0:
        left += 1  # we need a triplet with a bigger sum
      else:
        right -= 1  # we need a triplet with a smaller sum

  return target_sum - smallest_difference


def main():
  print(triplet_sum_close_to_target([-2, 0, 1, 2], 2))
  print(triplet_sum_close_to_target([-3, -1, 1, 2], 1))
  print(triplet_sum_close_to_target([1, 0, 1, 1], 100))


main()