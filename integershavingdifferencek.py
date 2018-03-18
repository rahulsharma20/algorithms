# Given an array of distinct integer values, count the number of pairs that have difference k

def differenceKIntegersPairCount(arr, k):
    if len(arr) == 0:
        return 0
    k = abs(k)
    arrayDict = {}
    count = 0
    finalArray = []

    for elem in arr:
       if elem not in arrayDict:
           arrayDict[elem] = 1

    for elem in arr:
        if elem + k in arrayDict:
            count = count + 1
            finalArray.append([elem, elem + k])

    return finalArray

if __name__ == "__main__":
    array = [1, 7, 9, 5, 2, 12, 3]
    k = 2

    pairs = differenceKIntegersPairCount(array, k)
    count = len(pairs)

    print pairs
