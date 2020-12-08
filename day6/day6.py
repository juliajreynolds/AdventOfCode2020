def findTotalYes(filename):
    all_group_responses = []
    total_yes = 0
    with open(filename, "r") as fp:
        current_group_set = set()
        for entry in fp:

            entry = entry.replace('\n', '')

            if len(entry) >= 1:
                letters = [char for char in entry]
                for letter in letters:
                    current_group_set.add(letter)
            else:
                all_group_responses.append(current_group_set)
                current_group_set = set()
    # get the last entry
    all_group_responses.append(current_group_set)

    for group_response in all_group_responses:
        total_yes += len(group_response)

    return total_yes


def findTotalUnanimousYes(filename):
    total_unanimous_yes = 0
    all_group_responses = []
    with open(filename, "r") as fp:
        current_group_set = set()
        common_group_choices = set()
        for entry in fp:

            entry = entry.replace('\n', '')

            if len(entry) >= 1:
                entrySet = frozenset(entry)
                current_group_set.add(entrySet)
            else:
                common_group_choices = set.intersection(*[set(x) for x in current_group_set])
                all_group_responses.append(common_group_choices)
                current_group_set = set()
        # get the last entry
    common_group_choices = set.intersection(*[set(x) for x in current_group_set])
    all_group_responses.append(common_group_choices)

    for group_response in all_group_responses:
        total_unanimous_yes += len(group_response)

    return total_unanimous_yes

if __name__ == "__main__":
    result1 = findTotalUnanimousYes("input.txt")
    print(result1)
