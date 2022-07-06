# Given an array of sorted numbers, remove all duplicate number instances from it in-place,
# such that each element appears only once. The relative order of the elements should be kept
# the same and you should not use any extra space so that that the solution have a space complexity of O(1).

# Move all the unique elements at the beginning of the array and after moving return the length of
# the subarray that has no duplicate in it.

# Input: [2, 3, 3, 3, 6, 9, 9]
# Output: 4
# Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].

# Input: [2, 2, 2, 11]
# Output: 2
# Explanation: The first two elements after removing the duplicates will be [2, 11].


# Using extra space
def remove_duplicates_space(arr):
  arr_dict = {}
  count = 0

  for e in arr:
    if e in arr_dict:
      count += 1
    else:
      arr_dict[e] = 1

  return len(arr) - count


arr = [2, 3, 3, 3, 6, 9, 9]


def remove_duplicates(arr):
  start = 0
  end = 1
  len_arr = len(arr)
  count = 0

  if len_arr < 2:
    return

  while (start < len_arr):
    if arr[start] != arr[end-1]:
      arr[end] = arr[start]
      end += 1
    start += 1

  return end


print (remove_duplicates(arr))


def remove_duplicates(arr):
  # index of the next non-duplicate element
  next_non_duplicate = 1

  i = 0
  while(i < len(arr)):
    if arr[next_non_duplicate - 1] != arr[i]:
      arr[next_non_duplicate] = arr[i]
      next_non_duplicate += 1
    i += 1

  print (arr)
  return next_non_duplicate


def main():
  print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
  print(remove_duplicates([2, 2, 2, 11]))


main()


