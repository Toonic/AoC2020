inArray = []

def input():
    with open("input2.txt") as file:
        for line in file:
            inArray.append(line)

input()

validCount = 0
part2Count = 0

for passIn in inArray:
    splitPass = passIn.split(':')
    minCount = int(splitPass[0].split('-')[0])
    maxCount = int(splitPass[0].split('-')[1].split(' ')[0])
    passRule = splitPass[0].split('-')[1].split(' ')[1]
    passWord = splitPass[1].replace(" ", "")
    count = 0

    for char in passWord:
        if char == passRule:
            count += 1
    if minCount <= count <= maxCount:
        validCount += 1

    if passWord[minCount - 1] == passRule:
        if passWord[maxCount - 1] != passRule:
            part2Count += 1
    if passWord[maxCount - 1] == passRule:
        if passWord[minCount - 1] != passRule:
            part2Count += 1

    
print("Part 1: " + str(validCount))
print("Part 2: " + str(part2Count))

