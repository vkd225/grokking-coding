# Given a list of non-overlapping intervals sorted by their start time, insert a given interval at the
# correct position and merge all necessary intervals to produce a list that has only mutually
# exclusive intervals.

# Example 1:
# Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,6]
# Output: [[1,3], [4,7], [8,12]]
# Explanation: After insertion, since [4,6] overlaps with [5,7], we merged them into one [4,7].

# Example 2:
# Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,10]
# Output: [[1,3], [4,12]]
# Explanation: After insertion, since [4,10] overlaps with [5,7] & [8,12], we merged them into [4,12].

# Example 3:
# Input: Intervals=[[2,3],[5,7]], New Interval=[1,4]
# Output: [[1,4], [5,7]]
# Explanation: After insertion, since [1,4] overlaps with [2,3], we merged them into one [1,4].



# [[1,3], [5,7], [8,12]] New Interval=[4,10]
# [[1,3], [4,12]]


# compare new_interval with intervals
# if new_interval.start < interval.end
  # while new_interval.end > this interval.end, next interval.end
    # interval.end = max(interval.end, max_end)


def insert_interval(intervals, new_interval):

  inserted_intervals = []

  for i in range(len(intervals)):

    if new_interval[0] < intervals[i][1]: #found the overlap
      j = i
      while (new_interval[1] > intervals[j][1]):
        start = min(new_interval[0], intervals[j][0])

        j += 1

        end = max(new_interval[1], intervals[j][1])


      inserted_intervals.append([start, end])

    else:
      inserted_intervals.append(intervals[i])

  return inserted_intervals



intervals = [[1,3], [3,7], [8,12]]
new_interval = [4,10]

# print (insert_interval(intervals, new_interval))






def insert(intervals, new_interval):
  merged = []
  i, start, end = 0, 0, 1

  # skip (and add to output) all intervals that come before the 'new_interval'
  while i < len(intervals) and intervals[i][end] < new_interval[start]:
    merged.append(intervals[i])
    i += 1

  # merge all intervals that overlap with 'new_interval'
  while i < len(intervals) and intervals[i][start] <= new_interval[end]:
    new_interval[start] = min(intervals[i][start], new_interval[start])
    new_interval[end] = max(intervals[i][end], new_interval[end])
    i += 1

  # insert the new_interval
  merged.append(new_interval)

  # add all the remaining intervals to the output
  while i < len(intervals):
    merged.append(intervals[i])
    i += 1
  return merged


def main():
  print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 6])))
  print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 10])))
  print("Intervals after inserting the new interval: " + str(insert([[2, 3], [5, 7]], [1, 4])))


main()
