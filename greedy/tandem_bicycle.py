def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds.sort()

    if fastest :
        blueShirtSpeeds.sort(reverse=True)
    else:
        blueShirtSpeeds.sort()

    sum = 0
    for i in range(len(blueShirtSpeeds)):
        max_speed= max(blueShirtSpeeds[i], redShirtSpeeds[i])
        sum += max_speed

    return sum
