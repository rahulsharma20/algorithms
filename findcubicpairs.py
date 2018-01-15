# Print all positive solutions to the equation a^3 + b^3 = c^3 + d^3
# where a, b, c, d are integers between 1 and 1000
import timeit

def findCubicPairs(n):
    hashMap = {}
    pairs = []
    for i in range(1, n+1):
        for j in range(1, n+1):
            cubicSum = (i*i*i)+(j*j*j)
            if cubicSum in hashMap and (hashMap[cubicSum] != [i,j] or hashMap[cubicSum] != [j,i]):
                pairFound = [hashMap[cubicSum][0],hashMap[cubicSum][1], i, j]
                pairs.append(pairFound)
            else:
                hashMap[cubicSum] = [i,j]

    return pairs

if __name__ == "__main__":
    # Start timer
    start = timeit.default_timer()

    n = 1000
    cp = findCubicPairs(n)

    # Stop timer
    stop = timeit.default_timer()

    print stop - start
