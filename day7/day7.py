def part1(bags, stringNeeded):
    bagsList = []
    for x in bags:
        findBag = x.find(' bags contain')
        if stringNeeded in x[findBag:]:
            bagsList.append(x[:findBag])
            bagsList.extend(part1(bags, x[:findBag]))
    return bagsList

def parseShinyBags(filename):
    myFile = open(filename, "r")
    content = myFile.read().splitlines()
    return len(set(part1(content, "shiny gold")))

# def countBagsInsideGold(filename):
#     myFile = open(filename, "r")
#     content = myFile.read().split('\n')
#     allBags = {}
#
#     for line in content:
#         line = line.replace("bags", "").replace("bag", "").strip(".")
#         line = line.split("contain")
#         allBags[line[0].strip()] = line[1].strip().split(',')
#
# def getBag(bags):
#     total = 1
#     if "no other" in allBags[bags]:
#         return 1
#     for colours in allBags[bags]:
#         each = colours.split()
#         total += int(each[0]) * getBag(" ".join(each[1:]))
#     return total
#
#
# print(getBag("shiny gold")-1)


if __name__ == "__main__":
    print(parseShinyBags("input.txt"))





