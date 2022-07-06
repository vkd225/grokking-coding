k =5
arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]

def moving_average (arr, k):
	summation = 0.0
	result = []
	start = 0

	for i in range (len(arr)):
		
		summation = (summation + arr[i])

		if (i >= k-1):
			result.append(summation/k)
			summation = summation - arr[start]
			start = start + 1


	return result


print moving_average(arr, k)



def find_averages_of_subarrays(K, arr):
  result = []
  windowSum, windowStart = 0.0, 0
  for windowEnd in range(len(arr)):
    windowSum += arr[windowEnd]  # add the next element
    # slide the window, we don't need to slide if we've not hit the required window size of 'k'
    if windowEnd >= K - 1:
      result.append(windowSum / K)  # calculate the average
      windowSum -= arr[windowStart]  # subtract the element going out
      windowStart += 1  # slide the window ahead

  return result


def main():
  result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
  print("Averages of subarrays of size K: " + str(result))


main()