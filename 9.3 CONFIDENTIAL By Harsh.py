inputString = input("Please Enter The Input String : ")
stringList = list(inputString)
alphabetList = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z"]
swappedStringList = []
if len(inputString) % 2 == 0:
    for i in range(0, len(inputString), 2):
        t = stringList[i]
        stringList[i] = stringList[i+1]
        stringList[i+1] = t
        swappedString = "".join(stringList)
else:
    for i in range(0, len(inputString) - 1, 2):
        t = stringList[i]
        stringList[i] = stringList[i+1]
        stringList[i+1] = t
        swappedString = "".join(stringList)
swappedStringList = list(swappedString)
for k in range(0, len(alphabetList)):
    if swappedString.__contains__(alphabetList[k]):
        positionOfLetter = [i for i, letter in enumerate(swappedString) if letter == alphabetList[k]]
        for i in range(len(positionOfLetter)):
            letterToBeReplaced = swappedString[positionOfLetter[i]]
            indexOfLetterInAlphabetList = alphabetList.index(letterToBeReplaced)
            alphabetToBeReplacedWith = alphabetList[-1-indexOfLetterInAlphabetList]
            swappedStringList[positionOfLetter[i]] = alphabetToBeReplacedWith
            replacedString = "".join(swappedStringList)
print(replacedString)