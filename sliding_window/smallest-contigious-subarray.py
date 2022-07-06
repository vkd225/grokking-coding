import sys
import math


# Wrong - move or decrease the start pointer and move the end pointer

# def smallest_contigious_subarray (arr, S):

# 	len_smallest = sys.maxsize

# 	len_moving_sub_array = 0
# 	moving_sum = 0

# 	for start in range (len(arr)):

# 		if moving_sum < S:

# 			moving_sum += moving_sum + arr[]

# 			len_moving_sub_array += 1


# 		elif moving_sum >= S: 

# 			print len_moving_sub_array

# 			len_smallest = min(len_smallest, len_moving_sub_array)

# 			end, start = start + 1

# 			moving_sum = arr[start]
# 			len_moving_sub_array = 1

# 	print "output"

# 	return len_smallest


# print smallest_contigious_subarray(arr, S)





def smallest_contigious_subarray(arr, S):
	start = 0
	moving_sum = 0

	min_len = sys.maxsize

	for end in range (len(arr)):

		moving_sum += arr[end]

		while moving_sum >= S:
			min_len = min(min_len, end-start+1)
			moving_sum -= arr[start]
			start += 1


	return min_len




print smallest_contigious_subarray(arr, S)

import math


def smallest_subarray_sum(s, arr):
  
  min_length = math.inf
  window_sum = 0
  window_start = 0
  for window_end in range(0, len(arr)):
      window_sum += arr[window_end]  # add the next element
    # shrink the window as small as possible until the 'window_sum' is smaller than 's'
      while window_sum >= s:
        min_length = min(min_length, window_end - window_start + 1)
        window_sum -= arr[window_start]
        window_start += 1
      
  if min_length == math.inf:
    return 0
  return min_length


def main():
  print("Smallest subarray length: " + str(smallest_subarray_sum(7, [2, 1, 5, 2, 3, 2])))
  print("Smallest subarray length: " + str(smallest_subarray_sum(8, [3, 4, 1, 1, 6])))
  print("Smallest subarray length: " + str(smallest_subarray_sum(8, [2, 1, 5, 2, 3, 2])))
  print("Smallest subarray length: " + str(smallest_subarray_sum(14, [1,14,3,3,4,4,4,4,4])))



main()
