# You are given an array of integers nums, there is a sliding window of size k which is moving
# from the very left of the array to the very right. You can only see the k numbers in the window.
# Each time the sliding window moves right by one position.

# Return the max sliding window


# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# 1 2 3 4 5 6 7 8 9
# Output: [3,3,5,5,6,7]
# Explanation:
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7


# 1, 3, -1, -3, 5, 3, 6, 7
# 3, 3, 5, 5, 6, 7

# slide and window



def sliding_window_maximum (arr, k):
  start = 0
  result_arr = []

  window_max = float("-inf")

  if type(k) is not int:
    return "Invalid K"

  if len(arr) == 0:
    return "Empty array"

  for end in range(len(arr)):
    if (end == k-1):
      window_max = max(arr[start], arr[start + 1])
      window_max = max(window_max, arr[end])

      result_arr.append(window_max)

    elif (end > k - 1):
      if window_max != arr[start]:
        window_max = max(window_max, arr[end])
      else:
        window_max = max(arr[start + 1], arr[start+2])
        window_max = max(window_max, arr[end])

      start += 1
      result_arr.append(window_max)

  return result_arr

arr = [1,2,3,4,5,6,7,8,9]
k = 3
print (sliding_window_maximum(arr, k))

