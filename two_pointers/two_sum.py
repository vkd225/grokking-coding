# Input: [1, 2, 3, 4, 6], target=6
# Output: [1, 3]
# Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6

# Input: [2, 5, 9, 11], target=11
# Output: [0, 2]
# Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11


def pair_with_targetsum(arr, target_sum):
  len_arr = len(arr)
  start = 0
  end = len_arr - 1

  for i in range(len_arr):
    if (arr[start] + arr[end]) == target_sum:
      return [start, end]
    else:
      if (arr[start] + arr[end]) > target_sum:
        end -= 1
      else:
        start += 1

  return [-1, -1]

def main():
  print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
  print(pair_with_targetsum([2, 5, 9, 11], 11))


main()