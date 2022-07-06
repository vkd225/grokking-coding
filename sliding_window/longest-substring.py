string = "araacasdasdi"
k =2

# Input: String="araaci", K=2
# Output: 4
# Explanation: The longest substring with no more than '2' distinct characters is "araa".

# a s d a a d q e

import math

def longest_substring(string, k):
	result = 0

	chars_dict = {}
	start = 0
	moving_dist_chars = 0

	for end in range (len(string)):

		moving_dist_chars += 1

		if (string[end] in chars_dict):

			chars_dict[string[end]] = chars_dict.get(string[end]) + 1
		else:

			chars_dict[string[end]] = 1


		while len(chars_dict) > k:

		

			chars_dict[string[start]] = chars_dict.get(string[start]) - 1


			if  chars_dict[string[start]] == 0:
				chars_dict.pop(string[start])

			moving_dist_chars -= 1
			start += 1

		result = max(result, end-start +1)


	return result

print (longest_substring(string, k))




def longest_substring_with_k_distinct(str1, k):
  window_start = 0
  max_length = 0
  char_frequency = {}

  # in the following loop we'll try to extend the range [window_start, window_end]
  for window_end in range(len(str1)):
    right_char = str1[window_end]
    if right_char not in char_frequency:
      char_frequency[right_char] = 0
    char_frequency[right_char] += 1

    # shrink the sliding window, until we are left with 'k' distinct characters in the char_frequency
    while len(char_frequency) > k:
      left_char = str1[window_start]
      char_frequency[left_char] -= 1
      if char_frequency[left_char] == 0:
        del char_frequency[left_char]
      window_start += 1  # shrink the window
    # remember the maximum length so far
    max_length = max(max_length, window_end-window_start + 1)
  return max_length


 def main():
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 2)))
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 1)))
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("cbbebi", 3)))


main()
















