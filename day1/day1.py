
def find2020Product(filename):
    with open(filename, "r") as fp:
        expenses = set(map(int, fp))

        for amount1 in expenses:
            amount2 = 2020 - amount1
            if amount2 in expenses:
                return amount1 * amount2


if __name__ == "__main__":
    result = find2020Product("input.txt")
    print(result)
