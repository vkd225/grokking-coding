def nonConstructibleChange(coins):
    current_sum = 0

    coins.sort()

    for c in coins:
        if c > current_sum + 1:
            return current_sum + 1
        current_sum += c


    return current_sum + 1

