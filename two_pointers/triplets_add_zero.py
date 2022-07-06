# Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

# Input: [-3, 0, 1, 2, -1, 1, -2]
# Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
# Explanation: There are four unique triplets whose sum is equal to zero.


# sort the array first
# Create 3 pointers
# A pointer points to first element
  # and X pointer to start from second and another Y from third element
    # if -(x+y) == A, append that
# Move pointer A
  # x = A + 1
  # Y = A + 2
# Finish when A == len(arr)

def two_sum(arr, target_sum, start, triplets):

  end = len(arr)-1

  while (start < end):
    current_sum = arr[start] + arr[end]
    if current_sum == target_sum:
      triplets.append([-target_sum, arr[start], arr[end]])
      start += 1
      end -= 1
      while start < end and arr[start] == arr[start - 1]:  # skip same element to avoid duplicate triplets
        start += 1
      while start < end and arr[end] == arr[end + 1]:  # skip same element to avoid duplicate triplets
        end -= 1
    elif target_sum > current_sum:
      start += 1
    else:
      end -= 1




def triplets_add_zero(arr):
  arr.sort()

  triplets = []

  for i in range(len(arr)):
    if i > 0 and arr[i] == arr[i-1]:  # skip same element to avoid duplicate triplets
     continue
    triplet = two_sum(arr, -arr[i], i+1, triplets)

  return triplets


arr = [-3, 0, 1, 2, -1, 1, -2]
print (triplets_add_zero(arr))


