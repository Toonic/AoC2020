import re

inArray = []
matchCheck = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

def input():
    with open("input4.txt") as file:
        for line in file:
            inArray.append(line)
    inArray.append('\n')

input()

validCountPart1 = 0
validCountPart2 = 0
togetherInput = ""

def checkByr(inStr=""):
    if 1920 <= int(inStr.split("byr:")[1].split(" ")[0]) <= 2002:
        return(True)
    else:
        return(False)

def checkIyr(inStr=""):
    if 2010 <= int(inStr.split("iyr:")[1].split(" ")[0]) <= 2020:
        return(True)
    else:
        return(False)

def checkEyr(inStr=""):
    if 2020 <= int(inStr.split("eyr:")[1].split(" ")[0]) <= 2030:
        return(True)
    else:
        return(False)

def checkHgt(inStr=""):
    if "cm" in inStr.split("hgt:")[1].split(" ")[0]:
        if 150 <= int(re.findall(r'\d+',inStr.split("hgt:")[1].split(" ")[0])[0]) <= 193:
            return(True)
        else:
            return(False)
    elif "in" in inStr.split("hgt:")[1].split(" ")[0]:
        if 59 <= int(re.findall(r'\d+',inStr.split("hgt:")[1].split(" ")[0])[0]) <= 76:
            return(True)
        else:
            return(False)
    else:
        return(False)

def checkHcl(inStr=""):
    if re.search(r'^#(?:[0-9a-fA-F]{1,2}){6}$', inStr.split("hcl:")[1].split(" ")[0]):
        return(True)
    else:
        return(False)

def checkEcl(inStr=""):
    eyeColors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if any(x in inStr for x in eyeColors):
        return(True)
    else:
        return(False)
    
def checkPid(inStr=""):
    if len(inStr.split("pid:")[1].split(" ")[0]) == 9:
        return(True)
    else:
        return(False)

for i in range(len(inArray)):
    if inArray[i].isspace():
        if all(x in togetherInput for x in matchCheck):
            if checkByr(togetherInput) and checkIyr(togetherInput) and checkEyr(togetherInput) and checkHgt(togetherInput) and checkEcl(togetherInput) and checkHcl(togetherInput) and checkPid(togetherInput):
                validCountPart2 += 1
            validCountPart1 += 1
            togetherInput = ""
        else:
            togetherInput = ""
    else:
        togetherInput += " " + inArray[i].strip()

print("Part 1: " + str(validCountPart1))
print("Part 2: " + str(validCountPart2))

