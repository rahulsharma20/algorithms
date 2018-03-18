# Determine if a string has all unique characters

def isUnique(string):
    hashMap = {}

    for char in string:
        if char in hashMap:
            return False
        else:
            hashMap[char] = True

    return True

if __name__ == "__main__":
    stringWithDupes = 'somerandomstrigwithduplicates'
    uniqueString = 'asdfghjklqwertyuiop'

    if isUnique(stringWithDupes):
        print(stringWithDupes + " : String is unique")
    else:
        print(stringWithDupes + " : String has duplicate characters")

    if isUnique(uniqueString):
        print(uniqueString + " : String is unique")
    else:
        print(uniqueString + " : String has duplicate characters")
