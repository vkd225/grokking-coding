# Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=3
# Output: 6
# Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.

# [0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1]


def longest_subarry(arr, k):

  max_replace_count = 0
  max_count = 0
  start = 0
  arr_freq = {}

  for end in range(len(arr)):

    if arr[end] not in arr_freq:
      arr_freq[arr[end]] = 0
    arr_freq[arr[end]] += 1

    max_replace_count = max(max_replace_count, arr_freq[arr[end]])

    if (end - start + 1 - max_replace_count)  > k:
      arr_freq[arr[start]] -= 1
      start += 1

    max_count = max(max_count, end - start + 1)

  return max_count

arr = [0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1]
k = 3

print (longest_subarry(arr, k))



