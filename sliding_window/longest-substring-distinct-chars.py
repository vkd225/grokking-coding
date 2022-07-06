# Input: String="aabccbb"
# Output: 3
# Explanation: The longest substring with distinct characters is "abc".


# Input: String="abbbb"
# Output: 2
# Explanation: The longest substring with distinct characters is "ab".


# a b c b d b e b

# a a a b c c b b

# 0 1 2 3 4 5 6


# pseudocode

def longest_substring_distinct_chars(string):

	max_distinct_char = 0
	start = 0
	chars_freq_distict = {}


	for end in range (len(string)):

		r_char = string[end]

		if r_char in chars_freq_distict:
			start = max(start, (chars_freq_distict[r_char] + 1))

		chars_freq_distict[r_char] = end

		max_distinct_char = max(max_distinct_char, end - start + 1)

	return max_distinct_char

string = "abbbb"

# print (longest_substring_distinct_chars(string))


def non_repeat_substring(str1):
  window_start = 0
  max_length = 0
  char_index_map = {}

  # try to extend the range [windowStart, windowEnd]
  for window_end in range(len(str1)):
    right_char = str1[window_end]
    # if the map already contains the 'right_char', shrink the window from the beginning so that
    # we have only one occurrence of 'right_char'
    if right_char in char_index_map:
      # this is tricky; in the current window, we will not have any 'right_char' after its previous index
      # and if 'window_start' is already ahead of the last index of 'right_char', we'll keep 'window_start'
      window_start = max(window_start, char_index_map[right_char] + 1)
    # insert the 'right_char' into the map
    char_index_map[right_char] = window_end
    # remember the maximum length so far
    max_length = max(max_length, window_end - window_start + 1)
  return max_length


def main():
  print("Length of the longest substring: " + str(non_repeat_substring("aabccbb")))
  print("Length of the longest substring: " + str(non_repeat_substring("abbbb")))
  print("Length of the longest substring: " + str(non_repeat_substring("abccde")))


main()


# Length of the longest substring: 3
# Length of the longest substring: 2
# Length of the longest substring: 3











