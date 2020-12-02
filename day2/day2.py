import string

def countValidPasswords(filename):
    validCount = 0
    with open(filename, "r") as passwords:

        for entry in passwords:
            max_position, min_position, password, targetCharacter = parseInput(entry)
            password_letters = list(password)

            position_matches = 0
            if password_letters[min_position] == targetCharacter:
                position_matches += 1
            if password_letters[max_position] == targetCharacter:
                position_matches += 1
            if position_matches == 1:
                validCount += 1

    return validCount

def parseInput(entry):
    components = entry.split(":")
    configs = components[0]
    password = components[1]
    password = password.replace(' ', '')
    password = password.replace('/n', '')

    config_elements = configs.split(" ")
    min_max = config_elements[0].split("-")
    min_position = int(min_max[0]) - 1
    max_position = int(min_max[1]) - 1
    targetCharacter = config_elements[1]
    return max_position, min_position, password, targetCharacter

if __name__ == "__main__":
    result = countValidPasswords("input.txt")
    print(result)
