# Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
# Output: 5
# Explanation: We can put 3 'B' in one basket and two 'C' in the other basket. 
# This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']

# Input: Fruit=['A', 'B', 'C', 'A', 'C']
# Output: 3
# Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']


def fruits_in_basket(fruits):

	max_fruit = 0
	baskets = 2
	fruit_basket = {}

	start = 0

	for end in range(len(fruits)):

		end_fruit = fruits[end]

		if end_fruit not in fruit_basket:
			fruit_basket[end_fruit] = 0

		fruit_basket[end_fruit] += 1

		while len(fruit_basket) > baskets:
			start_fruit = fruits[start]

			fruit_basket[start_fruit] -= 1

			if fruit_basket[start_fruit] == 0:
				fruit_basket.pop(start_fruit)

			start += 1

		max_fruit = max(max_fruit, end - start + 1)


	return max_fruit


fruits = ['A', 'B', 'C', 'B', 'B', 'C']

print fruits_in_basket(fruits)



def fruits_into_baskets(fruits):
  window_start = 0
  max_length = 0
  fruit_frequency = {}

  # try to extend the range [window_start, window_end]
  for window_end in range(len(fruits)):
    right_fruit = fruits[window_end]
    if right_fruit not in fruit_frequency:
      fruit_frequency[right_fruit] = 0
    fruit_frequency[right_fruit] += 1

    # shrink the sliding window, until we are left with '2' fruits in the fruit frequency dictionary
    while len(fruit_frequency) > 2:
      left_fruit = fruits[window_start]
      fruit_frequency[left_fruit] -= 1
      if fruit_frequency[left_fruit] == 0:
        del fruit_frequency[left_fruit]
      window_start += 1  # shrink the window
    max_length = max(max_length, window_end-window_start + 1)
  return max_length


def main():
  print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
  print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))

main()


# Maximum number of fruits: 3
# Maximum number of fruits: 5


			






