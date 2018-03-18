# Given two strings, check if one is permutation of another
# Consideration 1. case sensitive (God is not a permutation of dog)
# Consideration 2. Whitespaces are significant ("god " is not a permutation of "dog")

def checkPermutation(string1, string2):
    if len(string1) != len(string2):
        return False

    hashMap = {}

    for char in string1:
        if char in hashMap:
            hashMap[char] = hashMap[char] + 1
        else:
            hashMap[char] = 1

    for char in string2:
        if char in hashMap:
            if hashMap[char] == 1:
                hashMap.pop(char, None)
            else:
                hashMap[char] = hashMap[char] - 1
        else:
            return False

    if len(hashMap) > 0:
        return False

    return True

if __name__ == "__main__":
    string1 = "god is god"
    string2 = "dog is dog"

    if (checkPermutation(string1, string2)):
        print("Is a permutation")
    else:
        print("Not a permutation")
