def sunsetViews(buildings, direction):
    stack = []
    last_val = 0

    if (direction == "EAST"):
        for i in range(len(buildings)-1, -1, -1):
            if buildings[i] > last_val:
                last_val = buildings[i]
                stack.insert(0, i)

    elif (direction == "WEST"):
        for i in range(len(buildings)):
            if buildings[i] > last_val:
                last_val = buildings[i]
                stack.append(i)

    return stack


