def sockMerchant(n, ar):
    socksDict = {}

    for i in ar:
        if (i in socksDict):
            socksDict[i] += 1
        else:
            socksDict[i] = 1

    returnVal = 0
    for kev, val in socksDict.items():
        returnVal += (val // 2)

    return returnVal


a = [10, 20, 20, 10, 10, 30, 50, 10, 20]

print (sockMerchant(9,a))