# # use https://www.programiz.com/python-programming/online-compiler/
DICTIONARY_WORDS = [ 'a', 'about', 'all', 'an', 'and', 'angel', 'are', 'as', 'at', 'be', 'but',
'by', 'can', 'do', 'dog', 'exchange', 'for', 'form', 'free', 'from', 'has', 'have', 'home', 'hope',
'if', 'in', 'info', 'information', 'is', 'it', 'life', 'more', 'my', 'new', 'no', 'not', 'of', 'on',
'one', 'or', 'other', 'our', 'page', 'search', 'that', 'the', 'this', 'to', 'us', 'was', 'we', 'will',
'with', 'you', 'your']

# THESAURUS = [
#   'search': ['find'],
#   'page': ['document'],
#   'exchange': ['switch', 'swap'],
#   'life': ['living'],
# ]

def isWord(phrase):
    return phrase in DICTIONARY_WORDS

# # This function should take a string argument phrase and returns the largest substring in phrase that is
# in dictionaryWords.

# mysearchpage

# informationsource



def create_sub_phrase(phrase, start, end):
  sub_string = "".join(phrase[start:end])


def getLargestWord(phrase):

  output = []

  for i, word in enumerate(DICTIONARY_WORDS):
    if word in phrase:
      output.append(word)

  max_len = 0
  largest_word = ""

  for w in output:
    if len(w) > max_len:
      max_len = len(w)
      largest_word = w

  return largest_word



# def getLargestWord(phrase):

# print('Test Cases for getLargestWord()')

print(getLargestWord('mysearchpage')) # 'search'

print(getLargestWord('informationsource')) # 'information'

print(getLargestWord('thispage')) # 'this'

print(getLargestWord('more')) # 'more'

print(getLargestWord('xyz')) # ''

print(getLargestWord('age')) # 'a'

# #  This function takes a string argument phrase and returns an array of the largest substring in phrase that is a dictionary word as well as any other dictionary words in the phrase, in the order that they appear in the phrase, always preferring largest words.
# def getLargestWordAndNeighbors(phrase) -> [str]:
#     return []

# print('Test Cases for getLargestWordAndNeighbors()')
# print(getLargestWordAndNeighbors('mysearchpage')) # ['my', 'search', 'page']

# print(getLargestWordAndNeighbors('hopexchangelife')) # ['exchange', 'life']

# print(getLargestWordAndNeighbors('phomeage'))  # ['home', 'a']

# print(getLargestWordAndNeighbors('angelifexchangeonexchangeinew')) # ['angel', 'if', 'exchange', 'on', 'exchange', 'new']

# print(getLargestWordAndNeighbors('xyz')) # []

# # This function shohuld call getLargestWordAndNeighbors and return an array of variations on phrase, where each variation substitutes one dictionary word with a synonym found in thesaurus.
# def getSynonymVariations(phrase) -> [str]:
#     return []

# print('Test Cases for getSynonymVariations()')
# print(getSynonymVariations('mysearchpage')) # ['myfindpage', 'mysearchdocument']

# print(getSynonymVariations('hopexchangelife')) # ['hopswitchlife', 'hopswaplife', 'hopexchangeliving']

# print(getSynonymVariations('xyzexchangexexchangexyz')) # ['xyzswitchxexchangexyz', 'xyzswapxexchangexyz','xyzexchangexswitchxyz', 'xyzexchangexswapxyz']



#  start = 0
#     end = 1



#     while end < len(phrase) and start < len(phrase):
#       sub_string = "".join(phrase[start:end])

#       is_present = False

#       print(sub_string, word)

#       if sub_string == word:
#         is_present = True

#       # is_present = isWord(sub_string)

#       if is_present:
#         if len(sub_string) > longest_sub_phrase_count:
#           longest_sub_phrase = sub_string
#           start = end

#       else:
#         if end < len(phrase):
#           end += 1

#         if end == len(phrase) - 1:
#           start += 1



#  longest_sub_phrase_count = 0
#     longest_sub_phrase = ""

#     while end < len(phrase) and start < len(phrase):
#       sub_string = "".join(phrase[start:end])

#       for i in range(len(DICTIONARY_WORDS)):



#       is_present = False

#       print(sub_string, word)

#       if sub_string == word:
#         is_present = True

#       # is_present = isWord(sub_string)

#       if is_present:
#         if len(sub_string) > longest_sub_phrase_count:
#           longest_sub_phrase = sub_string
#           start = end

#       else:
#         if end < len(phrase):
#           end += 1

#         if end == len(phrase) - 1:
#           start += 1


#     return longest_sub_phrase