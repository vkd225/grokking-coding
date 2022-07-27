def runLengthEncoding(string):
    output = ""
    start = 1
    for i in range(1, len(string)):
        print(output)
        if string[i] != string[i-1] or start == 9:
            output += str(start) + string [i-1]
            start = 0

        start += 1

    output  += str(start) + string[len(string) - 1]

    return output