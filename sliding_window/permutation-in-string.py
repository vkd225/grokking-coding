# Input: String="oidbcaf", Pattern="abc"
# Output: true
# Explanation: The string contains "bca" which is a permutation of the given pattern.

# a a a c b
# abc

def find_permutation(str1, pattern):
  max_chars = len (pattern)
  start = 0
  sub_pattern = []
  chars_freq = {}
  chars_freq_check = {}


  for i in range(len(pattern)):
    char = pattern[i]
    if char not in chars_freq:
      chars_freq[char] = 0
    chars_freq[char] += 1

  for end in range(len(str1)):

    sub_pattern.append(str1[end])

    if end >= (len(pattern)-1):
      # do something
      # check if the sub array is in the chars_freq
      # if true return true

      for char in sub_pattern:
        if char in chars_freq:
          if char not in chars_freq_check:
            chars_freq_check[char] = 0

          chars_freq_check[char] += 1

        else:
          chars_freq_check ={}

      if (chars_freq != chars_freq_check):
        chars_freq_check ={}
      else:
        return True

  return False


str1="aaacb"
pattern="abc"
print (find_permutation(str1, pattern))


# Solution#
# This problem follows the Sliding Window pattern, and we can use a similar sliding window strategy as discussed in Longest Substring with K Distinct Characters.
# We can use a HashMap to remember the frequencies of all characters in the given pattern. Our goal will be to match all the characters from this HashMap
# with a sliding window in the given string. Here are the steps of our algorithm:

# Create a HashMap to calculate the frequencies of all characters in the pattern.
# Iterate through the string, adding one character at a time in the sliding window.
# If the character being added matches a character in the HashMap, decrement its frequency in the map. If the character frequency becomes zero, we got a complete match.
# If at any time, the number of characters matched is equal to the number of distinct characters in the pattern (i.e., total characters in the HashMap), we have gotten our required
# permutation.
# If the window size is greater than the length of the pattern, shrink the window to make it equal to the pattern’s size. At the same time, if the character going out was part of
# the pattern, put it back in the frequency HashMap.


def find_permutation(str1, pattern):
  window_start, matched = 0, 0
  char_frequency = {}

  for chr in pattern:
    if chr not in char_frequency:
      char_frequency[chr] = 0
    char_frequency[chr] += 1

  # our goal is to match all the characters from the 'char_frequency' with the current window
  # try to extend the range [window_start, window_end]
  for window_end in range(len(str1)):
    right_char = str1[window_end]
    if right_char in char_frequency:
      # decrement the frequency of matched character
      char_frequency[right_char] -= 1
      if char_frequency[right_char] == 0:
        matched += 1

    if matched == len(char_frequency):
      return True

    # shrink the window by one character
    if window_end >= len(pattern) - 1:
      left_char = str1[window_start]
      window_start += 1
      if left_char in char_frequency:
        if char_frequency[left_char] == 0:
          matched -= 1
        char_frequency[left_char] += 1

  return False


def main():
  print('Permutation exist: ' + str(find_permutation("oidbcaf", "abc")))
  print('Permutation exist: ' + str(find_permutation("odicf", "dc")))
  print('Permutation exist: ' + str(find_permutation("bcdxabcdy", "bcdyabcdx")))
  print('Permutation exist: ' + str(find_permutation("aaacb", "abc")))


main()


