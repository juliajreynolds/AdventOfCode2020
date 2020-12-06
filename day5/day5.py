
def findMaxSeatID(filename):
    boarding_passes_binary, boarding_passes_decimal = findSeatIDs(filename)

    boarding_passes_decimal.sort(reverse=True)
    #print(boarding_passes_binary)
    #print(boarding_passes_decimal)

    return boarding_passes_decimal[0]


def findSeatIDs(filename):
    boarding_passes_binary = []
    boarding_passes_decimal = []
    populateBoardingPassesFromFile(filename, boarding_passes_binary)
    for binary_pass in boarding_passes_binary:
        seatid = binaryToDecimal(int(binary_pass))
        boarding_passes_decimal.append(seatid)
    return boarding_passes_binary, boarding_passes_decimal


def findEmptySeatID(filename):
    boarding_passes_binary, boarding_passes_decimal = findSeatIDs(filename)

    boarding_passes_decimal.sort()

    index = 0
    emptySeatID = 0

    while index < len(boarding_passes_decimal) :
        seatID = boarding_passes_decimal[index]
        nextSeatID = boarding_passes_decimal[index+1]

        if nextSeatID != seatID + 1 :
            emptySeatID = seatID + 1
            index = len(boarding_passes_decimal)

        index += 1

    return(emptySeatID)


def populateBoardingPassesFromFile(filename, boardingPasses):
    with open(filename, "r") as fp:
        for entry in fp:
            entry = entry.replace('\n', '')
            entry = entry.replace('B', '1')
            entry = entry.replace('F', '0')
            entry = entry.replace('R', '1')
            entry = entry.replace('L', '0')

            boardingPasses.append(entry)

    # Function calculates the decimal equivalent
    # to given binary number


def binaryToDecimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while (binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    #print(decimal)
    return decimal

if __name__ == "__main__":
    result1 = findMaxSeatID("input.txt")
    result2 = findEmptySeatID("input.txt")
    print(result1)
    print(result2)
