# find the first unique element in an array

arr = [1,2,4,1,5,-1,5,5,1,1,2,2,4]

# 1, 2, 4, 5, 5, 5, 1, 2, 2

# output = 4


def first_unique_element(arr):

  char_freq = {}

  for i in range(len(arr)):
    char = arr[i]

    if char in char_freq:
      char_freq[char] += 1
    else:
      char_freq[char] = 1

  for char in arr:
    if char_freq[char] == 1:
      return char

print (first_unique_element(arr))

