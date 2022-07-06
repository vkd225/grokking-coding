# Given a list of intervals,
# merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.

# Intervals: [[1,4], [2,5], [7,9]]
# Output: [[1,5], [7,9]]
# Explanation: Since the first two intervals [1,4] and [2,5] overlap, we merged them into
# one [1,5].

# Intervals: [[6,7], [2,4], [5,9]]
# Output: [[2,4], [5,9]]
# Explanation: Since the intervals [6,7] and [5,9] overlap, we merged them into one [5,9].

# Intervals: [[1,4], [2,6], [3,5]]
# Output: [[1,6]]
# Explanation: Since all the given intervals overlap, we merged them into one.


intervals = [[1,4], [2,6], [3,5]]
# [1,4], [2,6]
# Output: [[1,6]]


# sort the list, now a.start <= b.start
# if a.end > b.start then (a overlaps b) -- in this case,
#   start = a.start
#   end = max(a.end, b.end) results in 1,6 for first 2 array
# else doesn't overlap
#   print start, end

def merge_two_overlap(prev_window, cur_window):
  merged_window = []

  prev_start = prev_window[0]
  prev_end = prev_window[1]
  cur_start = cur_window[0]
  cur_end = cur_window[1]

  if cur_end > prev_start:
    cur_start = prev_start
    cur_end = max(prev_end, cur_end)

    merged_window.append(cur_start)
    merged_window.append(cur_end)

  return merged_window

def merge_overlap(intervals):

  if len(intervals) < 2:
    return intervals

  intervals.sort(key=lambda x: x[0])
  merged_intervals = []

  start = intervals[0][0]
  end = intervals[0][1]

  for i in range(1, len(intervals)):
    interval = intervals[i]

    if interval[0] <= end: # overlapping intervals, adjust the 'end'
      end = max(interval[1], end)
    else:
      merged_intervals.append([start, end]) # non-overlapping interval, add the previous internval and reset
      start = interval[0]
      end = interval[1]


  merged_intervals.append([start, end])
  return merged_intervals

intervals = [[1,4], [2,6], [3,5]]
print (merge_overlap(intervals))


# def merge(intervals):
  # list = []
  # if(len(intervals) < 2):
  #   return list

  # intervals.sort()

  # curr = intervals[0]

  # for i in intervals:
  #   if(curr[1] >= i[0]):
  #     curr[1] = max(curr[1], i[1])
  #   else:
  #     list.append(curr)
  #     curr = i

  # list.append(curr)
  # return list
