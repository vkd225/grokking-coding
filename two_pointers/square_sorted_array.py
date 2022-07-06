# Given a sorted array, create a new array containing squares of all the numbers of the input
# array in the sorted order.

# Input: [-2, -1, 0, 2, 3]
# Output: [0, 1, 4, 4, 9]

def create_sorted_squares(arr):

  arr_len = len(arr)
  start = 0
  end = arr_len -1
  insert_idx = end
  square_arr = [0] * arr_len

  while(start <= end):
    sq_st = arr[start] ** 2
    sq_end = arr[end] ** 2

    if sq_st >= sq_end:
      start += 1
      square_arr[insert_idx] = sq_st

    else:
      end -= 1
      square_arr[insert_idx] = sq_end

    insert_idx -= 1

  return square_arr

arr = [-2, -1, 0, 2, 3]
print (create_sorted_squares(arr))
