# Input: String="abbcabc", Pattern="abc"
# Output: [2, 3, 4]
# Explanation: The three anagrams of the pattern in the given string are "bca", "cab", and "abc".


# Attempt 1

def find_string_anagram(str1, pattern):

  pattern_freq = {}
  for char in pattern:
    if char not in pattern_freq:
      pattern_freq[char] = 0
    pattern_freq[char] += 1


  pattern_freq_copy = pattern_freq

  start = 0
  matched = 0
  result_arr = []

  for end in range(len(str1)):

    right_char = str1[end]
    if right_char in pattern_freq_copy:
      pattern_freq_copy[right_char] -= 1


      if pattern_freq_copy[right_char] == 0:
        matched += 1

      if len(pattern_freq_copy) == matched:
        result_arr.append(start)


    if end >= (len(pattern) - 1):
      left_char = str1[start]
      start += 1

      if left_char in pattern_freq_copy:
        matched -= 1

      pattern_freq_copy[left_char] += 1


    return result_arr


str1 = "abbcabc"
pattern = "abc"
print (find_string_anagram(str1, pattern))




