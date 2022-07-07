# Given an array nums of n integers where nums[i] is in the range [1, n],
# return an array of all the integers in the range [1, n] that do not appear in nums.

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]

def find_disappeared_nums(nums):
  result = []

  if len(nums) == 0:
    return result


  len_nums = len(nums)
  nums_dict = {}
  for i in range(len_nums):
    if nums[i] not in nums_dict:
      nums_dict[nums[i]] = i

  for i in range(1, len_nums+1):
    if i not in nums_dict:
      result.append(i)

  return result

nums = [4,3,2,7,8,2,3,1]
print(find_disappeared_nums(nums))



# The time complexity is O(2n) -> O(n) and the space complexity is O(1).


ans = []
N = len(nums)
i = 0
while (i < N):
	a = nums[i] - 1
	if nums[i] == i + 1:
		i = i + 1
	elif nums[i] == nums[a]:
		i = i + 1
	else:
		nums[i], nums[a] = nums[a], nums[i]

for i in range(N):
	if nums[i] != i + 1:
		ans.append(i + 1)
return ans