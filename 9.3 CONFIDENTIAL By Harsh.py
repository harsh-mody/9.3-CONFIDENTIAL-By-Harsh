inputString = input("Please Enter The Input String : ")
stringList = list(inputString)
alphabetList = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z"]
originalLetterList = []
letterToBeReplacedWithList = []
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
for i in range(0, len(alphabetList)):
    if swappedString.__contains__(alphabetList[i]):
        originalLetterList.append(alphabetList[i])
        letterToBeReplacedWithList.append(alphabetList[-1-i])
        replacedString = swappedString
        for k in range(0, len(letterToBeReplacedWithList)):
            replacedString = replacedString.replace(originalLetterList[k], letterToBeReplacedWithList[k])
print(replacedString)

