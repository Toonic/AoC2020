inArray = []
downmap = [1,1,1,1,2]
rightmap = [1,3,5,7,1]

countmap = [0,0,0,0,0]

def input():
    with open("input3.txt") as file:
        for line in file:
            inArray.append(line)

input()

endValue = 1

for mapIndex in range(len(downmap)):
    count = 0
    for i in range(0,len(inArray), downmap[mapIndex]):
        output = list(inArray[i])
        if count >= len(inArray[i]) - 1:
            count = (len(inArray[i]) - 1 - count) * -1
        if inArray[i][count] == "#":
            countmap[mapIndex] += 1
        count += rightmap[mapIndex]
    endValue *= countmap[mapIndex]

print("Part 1: " + str(countmap[1]))
print("Part 2: " + str(endValue))