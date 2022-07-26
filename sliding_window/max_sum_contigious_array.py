# Initialize:
#     max_so_far = INT_MIN
#     max_ending_here = 0

# Loop for each element of the array
#   (a) max_ending_here = max_ending_here + a[i]
#   (b) if(max_so_far < max_ending_here)
#             max_so_far = max_ending_here
#   (c) if(max_ending_here < 0)
#             max_ending_here = 0
# return max_so_far


def kadanesAlgorithm(array):
    start = 0
    end = 1
    total_sum = array[start]
    curr_sum = array[start]

    for i in range(1, len(array)):
        curr_sum = max(array[i], curr_sum + array[i])
        total_sum = max(curr_sum, total_sum)

    return total_sum

