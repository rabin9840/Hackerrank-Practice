def sockMerchant(n, ar):
    # Write your code here
    countDict = {}
    pairs = 0
    for value in ar:
        if value not in countDict:
            countDict[value] = 1
        else:
            countDict[value] += 1
        if countDict[value] == 2:
            pairs = pairs +1
            countDict[value] -= 2
    return pairs