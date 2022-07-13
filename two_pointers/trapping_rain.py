# Given n non-negative integers representing an elevation map where the width of each bar is 1,
# compute how much water it can trap after raining.

rain = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
output = 6


def trapping_rain(rain):
  rain_len = len(rain)

  left = 0
  right = rain_len - 1
  left_max = rain[0]
  right_max = rain[right]
  count = 0

  while (left < right):

    if rain[left] < rain[right]:
      left += 1
      left_max = max(left_max, rain[left])
      count += left_max - rain[left]

    else:
      right -= 1
      right_max = max(right_max, rain[right])
      count += right_max - rain[right]

  return count

print (trapping_rain(rain))


# https://leetcode.com/problems/trapping-rain-water/discuss/1374608/C%2B%2BJavaPython-MaxLeft-MaxRight-so-far-with-Picture-O(1)-space-Clean-and-Concise



