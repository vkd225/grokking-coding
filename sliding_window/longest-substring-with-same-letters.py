# Input: String="aabccbb", k=2
# Output: 5
# Explanation: Replace the two 'c' with 'b' to have the longest repeating substring "bbbbb".


# Input: String="abbcb", k=1
# Output: 4
# Explanation: Replace the 'c' with 'b' to have the longest repeating substring "bbbb".


# a b b c b


def longest_substring_with_same_letters(str1, k):

	start = 0
	max_len = 0
	char_freq = {}

	if 
