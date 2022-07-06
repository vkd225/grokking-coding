# smallest-substring-containing-all-chars.py

# Input: String="aabdec", Pattern="abc"
# Output: "abdec"
# Explanation: The smallest substring having all characters of the pattern is "abdec"

# Input: String="abdbca", Pattern="abc"
# Output: "bca"
# Explanation: The smallest substring having all characters of the pattern is "bca".


# a a b d e c
# a b c

# Output: "abdec"

#  Brute force
def get_all_substrings(str1):
  result = []
  final_result = []
  len_pattern = 3

  for i in range(len(str1)):
    for j in range(len_pattern + i, len(str1) + 1):
      result.append(str1[i:j])

  #  create an array of object
  for sub_string in result:
    sub_str_freq = {}
    for c in sub_string:
      if c not in sub_str_freq:
        sub_str_freq[c] = 0
      sub_str_freq[c] += 1

    final_result.append(sub_str_freq)

  return result, final_result


def check_if_all_chars_or_not(obj, pattern):
  for p in pattern:
    if p not in obj:
      return False

    obj[p] -= 1

    if obj[p] == 0:
      del obj[p]
  return True



def smallest_window_containting_all_chars_brute(str1, pattern):

  smallest_sub_pattern_len = float("inf")
  smallest_sub_pattern = ""

  arr, obj = get_all_substrings(str1)

  for i in range(len(obj)):

    imm_result = check_if_all_chars_or_not(obj[i], pattern)
    if imm_result is True:
      smallest_sub_pattern_len = min(smallest_sub_pattern_len, len(arr[i]))
      smallest_sub_pattern = arr[i]

  return smallest_sub_pattern


# print (smallest_window_containting_all_chars_brute("aabdec", "abc"))


# Input: String="aabdec", Pattern="abc"
# Output: "abdec"
# Explanation: The smallest substring having all characters of the pattern is "abdec"

# a a b d e c
# abc

# Output: "abdec"



def smallest_window_containting_all_chars(str1, pattern):
  start = 0
  smallest_sub = ""
  char_freq = {}
  pattern_freq = {}
  matched = 0

  for p in pattern:
    if p not in pattern_freq:
      pattern_freq[p] = 0
    pattern_freq[p] += 1


  for end in range(len(str1)):

    if str1[end] not in char_freq:
      str1[end] = 0
    str1[end] += 1

    # compare pattern to char_freq

    # if yes, everything is in char_freq, start += 1
    # if no, add str[end] to char_freq


def find_substring(str1, pattern):
  window_start, matched, substr_start = 0, 0, 0
  min_length = len(str1) + 1
  char_frequency = {}

  # a b c
  for chr in pattern:
    if chr not in char_frequency:
      char_frequency[chr] = 0
    char_frequency[chr] += 1

  # {a:  1, b: 1, c:1 }
  # a a b d e c
  # try to extend the range [window_start, window_end]

  for window_end in range(len(str1)):
    right_char = str1[window_end]

    if right_char in char_frequency:
      char_frequency[right_char] -= 1

      # char_freq = {a: 0, b: 1, c:1}

      if char_frequency[right_char] >= 0:  # Count every matching of a character
        matched += 1

    # Shrink the window if we can, finish as soon as we remove a matched character
    while matched == len(pattern):
      if min_length > window_end - window_start + 1:
        min_length = window_end - window_start + 1
        substr_start = window_start

      left_char = str1[window_start]
      window_start += 1
      if left_char in char_frequency:
        # Note that we could have redundant matching characters, therefore we'll decrement the
        # matched count only when a useful occurrence of a matched character is going out of the window
        if char_frequency[left_char] == 0:
          matched -= 1
        char_frequency[left_char] += 1

  if min_length > len(str1):
    return ""
  return str1[substr_start:substr_start + min_length]


def main():
  print(find_substring("aabdec", "abc"))
  print(find_substring("aabdec", "abac"))
  print(find_substring("abdbca", "abc"))
  print(find_substring("adcad", "abc"))

main()
















