# def build_word_tree_from_sentences(sentence_list):
#   root = {}
#   for sentence in sentence_list:
#     base = root
#     for word in sentence.split(' '):
#       if word not in base:
#         base[word] = {}
#       base = base[word]
#   return root

# tree = build_word_tree_from_sentences(["Hello world", "Hello there"])
# print (tree)

# f = lambda n: 1 if n <= 1 else n * f(n - 1)
# g = f(4)

# print (g)


# def collapse_consecutive_repeats(str):
#   seen = {}
#   accumulator = ""
#   for char in str:
#     if char not in seen:
#       accumulator = accumulator + char
#     seen[char] = True
#   return accumulator

# print (collapse_consecutive_repeats("abate"))


def mystery_function(input_str):
  i = len(input_str)
  accumulator = ""
  while i >= 0:
    accumulator = input_str[len(input_str) - i] + accumulator
    i = i - 1
  return accumulator

# print(mystery_function("abcde"))


x = {'foo': 'bar'}
y = {'baz': x}
z = y['baz']['foo']

print (z) # bar


def mystery_function(func, items):
  i = 0
  for item in items:
    if func(item):
      items[i] = item
      i += 1
  del items[i:]


  def map(array, method):
  result = []
  for element in array:
    value = method(element)
    # MISSING LINE
  return result
