# inp = [75, 105, 120, 75, 90, 135]
# dp = [75, 105, 195, 195, 285, 330]
# returns 330

def maxSubsetSumNoAdjacent(array):
    if not (len(array)):
        return 0
    elif len(array) == 1:
        return array[0]

    dp = array
    dp[1] = max(array[0], array[1])
    return max_sum_non_adjacent_elements(array, dp)

def max_sum_non_adjacent_elements(array, dp):
    for i in range(2, len(array)):
        dp[i] = max(dp[i-1], (dp[i-2]  + array [i]))

    return dp[-1]