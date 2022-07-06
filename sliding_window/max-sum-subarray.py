arr = [2,1,2,3,4,4,4,3]
k = 3


def max_sum_sub_array (arr, k):
	start = 0

	max_sum = 0
	moving_sum = 0

	for end in range (len(arr)):

		moving_sum += arr[end]

		if (end >= k-1):
			max_sum =  max (max_sum, moving_sum)
			moving_sum = moving_sum - arr[start]
			start = start + 1

	return max_sum

print max_sum_sub_array(arr, k)
