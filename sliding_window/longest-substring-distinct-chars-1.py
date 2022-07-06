# Input: String="aabccbb"
# Output: 3
# Explanation: The longest substring with distinct characters is "abc".


# Input: String="abccde"
# Output: 3
# Explanation: Longest substrings with distinct characters are "abc" & "cde".

# a b c c d e
# insert into the dict
# if not in dict, insesrt into dict, end += 1
# if in dict, start += 1
# keep a max_count


def longest_substring_distinct_chars (string):

  start = 0
  max_char_count = 0
  char_freq= {}

  for end in range(len(string)):

    right_char = string[end]

    if right_char in char_freq:
      start = max(start, end)

    else:
      char_freq[right_char] = end
      max_char_count = max(max_char_count, end - start +1)

  return max_char_count

print (longest_substring_distinct_chars("aabccbb"))



