import re


def countValidPassports(filename):
    valid_count = 0
    passports = []

    populatePassportsFromFile(filename, passports)
    print("found passports: " + str(len(passports)))
    for passport in passports:

        if len(passport.keys()) == 8:
            if validateFields(passport):
                valid_count += 1
        else:
            if len(passport.keys()) == 7:
                if "cid" not in passport.keys():
                    if validateFields(passport):
                        valid_count += 1
    return valid_count


def validateFields(passport):
    regexForBYR = r"(19[2-8][0-9]|199[0-9]|200[0-2])"
    regexForIYR = r"(201[0-9]|2020)"
    regexForEYR = r"(202[0-9]|2030)"
    regexForCM = r"(1[5-8][0-9]|19[0-3])cm$"
    regexForIN = r"(59|6[0-9]|7[0-6])in$"
    regexForWebColor = r"^#(?:[0-9a-fA-F]{6}){1,2}$"
    regexForEyeColor = r"^(amb|blu|brn|gry|grn|hzl|oth)$"
    regexForPID = r"^\d\d\d\d\d\d\d\d\d$"

    validFieldCount = 0

    validFields = False

    if re.match(regexForBYR, passport["byr"]) :
        validFieldCount += 1
    if re.match(regexForIYR, passport["iyr"]) :
        validFieldCount += 1
    if re.match(regexForEYR, passport["eyr"]) :
        validFieldCount += 1
    if re.match(regexForCM, passport["hgt"])  or re.match(regexForIN, passport["hgt"]) :
        validFieldCount += 1
    if re.match(regexForWebColor, passport["hcl"]) :
        validFieldCount += 1
    if re.match(regexForEyeColor, passport["ecl"]) :
        validFieldCount += 1
    if re.match(regexForPID, passport["pid"]) :
        validFieldCount += 1

    if validFieldCount == 7:
        validFields = True

    return validFields


def populatePassportsFromFile(filename, passports):
    total_passports = 1
    with open(filename, "r") as fp:

        passport = {}
        for entry in fp:
            entry = entry.replace('\n', '')

            if len(entry) > 1:
                pairs = entry.split(' ')
                for pair in pairs:
                    passport[pair.split(':')[0]] = pair.split(':')[1]
            else:
                total_passports += 1
                passports.append(passport)
                passport = {}
    passports.append(passport)
    print("total in file:" + str(total_passports))


if __name__ == "__main__":
    result1 = countValidPassports("input.txt")
    print(result1)
