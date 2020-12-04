inArray = []

def input():
    with open("input1.txt") as file:
        for line in file:
            inArray.append(int(line))

input()
inArray.sort()

for num in inArray:
    for num2 in inArray:
        if (num + num2 == 2020):
            print("Part 1: " + str(num * num2))
            break
    else:
        continue
    break

for num in inArray:
    for num2 in inArray:
        for num3 in inArray:
            if (num + num2 + num3 == 2020):
                print("Part 2: " + str(num * num2 * num3))
                break
        else:
            continue
        break
    else:
        continue
    break
    
