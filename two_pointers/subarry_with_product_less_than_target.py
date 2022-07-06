# Given an array with positive numbers and a positive target number,
# find all of its contiguous subarrays whose product is less than the target number.

# text = ['Python', 'is', 'a', 'fun', 'programming', 'language']

# # join elements of text with space
# print(' '.join(text))

# Output: Python is a fun programming language

# Input: [2, 5, 3, 10], target=30
# Output: [2], [5], [2, 5], [3], [5, 3], [10]
# Explanation: There are six contiguous subarrays whose product is less than the target.

# 2, 5, 3, 10

# brute force method
def subarry_with_product_less_than_target(arr, target):
  result = []
  for i in range(len(arr)):
    product = arr[i]
    j = i + 1

    while j < len(arr):
      product = product * arr[j]

      print ("prod: {}, target: {}".format(product, target))
      print (arr[i:j])

      # if product < target:
      #   # print (arr[i:j])
      # else:
      #   break

      j += 1

  # return

arr = [2, 5, 3, 10]
target=30
(subarry_with_product_less_than_target(arr, target))


