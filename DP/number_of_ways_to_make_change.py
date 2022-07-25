# bottom up approach

def numberOfWaysToMakeChange(n, denoms):
    ways_to_change = [0 for change in range(0, n+1)]

    ways_to_change[0] = 1

    for c in denoms:
        for amount in range(1, len(ways_to_change)):
            if c <= amount:
                ways_to_change[amount] += ways_to_change[amount - c]

    print ()
    return ways_to_change[-1]


