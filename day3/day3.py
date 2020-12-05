import string

def countTrees(filename,row_step,col_step):
    tree_count = 0
    with open(filename, "r") as fp:
        hillside_rows = list(fp)

        row_index = row_step
        col_index = col_step

        row_count = len(hillside_rows)

        while row_index < row_count:
            row = hillside_rows[row_index]
            row = row.replace('\n', '')

            while col_index >= len(row):
             #row = row + row
                col_index = col_index - 31

            target_row = list(row)
            target = target_row[col_index]

            if target == '#':
                tree_count += 1

            row_index += row_step
            col_index += col_step

    return tree_count

if __name__ == "__main__":
    result1 = countTrees("input.txt",1,1)
    print(result1)
    result2 = countTrees("input.txt", 1, 3)
    print(result2)
    result3 = countTrees("input.txt", 1, 5)
    print(result3)
    result4 = countTrees("input.txt", 1, 7)
    print(result4)
    result5 = countTrees("input.txt", 2, 1)
    print(result5)
    print(result1 * result2 * result3 * result4 * result5)
