# Given two lists of intervals, find the intersection of these two lists.
# Each list consists of disjoint intervals sorted on their start time.

# Input: arr1=[[1, 3], [5, 6], [7, 9]], arr2=[[2, 3], [5, 7]]
# Output: [2, 3], [5, 6], [7, 7]
# Explanation: The output list contains the common intervals between the two lists.

# I don't think 7,7 should be here

# Input: arr1=[[1, 3], [5, 7], [9, 12]], arr2=[[5, 10]]
# Output: [5, 7], [9, 10]
# Explanation: The output list contains the common intervals between the two lists.

# arr1=[[1, 3], [5, 7], [9, 12]],
# arr2=[[5, 10]]
#  Output: [5, 7], [9, 10]




# compare arr_2.start < with arr_1.end
# if true:
# take arr2.end and compare with arr1.start1 , arr1.start2 and move on

# start = max(arr1.start, arr2.start)
# end = min(arr1.end, arr2.end)
# output.append(max, min)
# start with arr_2 next item and arr_1 next item



def intervals_intersection(interval_a, interval_b):

  len_interval_a = len(interval_a)
  len_interval_b = len(interval_b)
  a = 0
  b = 0
  start = 0
  end = 1
  result = []

  while (a < len_interval_a and b < len_interval_b):

    # check if intervals overlap and intervals_a[i]'s start time lies within the other intervals_b[j]
    a_overlap_b = (interval_a[a][0] >= interval_b[b][0]) and (interval_a[a][0] <= interval_b[b][1] )

    # check if intervals overlap and intervals_b[j]'s start time lies within the other intervals_a[i]
    b_overlap_a = (interval_b[b][0] >= interval_a[a][0]) and (interval_b[b][0] <= interval_a[a][1])

    if (a_overlap_b or b_overlap_a):
      start = max(interval_a[a][0], interval_b[b][0])
      end = min (interval_a[a][1], interval_b[b][1])
      result.append([start, end])

    if interval_a[a][1] < interval_b[b][1]:
      a += 1
    else:
      b += 1

  return result


arr1=[[1, 3], [5, 6], [7, 9]]
arr2=[[2, 3], [5, 7]]
print (intervals_intersection(arr1, arr2))