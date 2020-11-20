import time


def check_complete(assignment, solSet):
    count = 0
    if assignment in solSet:
        return False
    for index, seat in enumerate(assignment):
        if seat != "0":
            count += 1
    v = False
    outset = set()
    for index, seat in enumerate(assignment):
        if seat != "0":
            for index2, seat2 in enumerate(assignment):
                if seat2 != "0":
                    if index != index2:
                        outset.add(abs(index - index2))

    if count == 5 and len(outset) == 10: return True
    return False


def select_unassigned_var(assignment):
    smol = None
    for index, trangle in enumerate(assignment):
        if trangle == "0":
            return index
    return smol


def isValid(value, var_index, assignment):
    outset = set()
    for index, seat in enumerate(assignment):
        if seat != "0":
            for index2, seat2 in enumerate(assignment):
                if seat2 != "0":
                    if index != index2:
                        outset.add(abs(index - index2))
    hTemp2 = outset.copy()
    count = 0
    for index, seat in enumerate(assignment):
        if seat != "0":
            if abs(index - var_index) in outset:
                return False
    # if len(hTemp2) == len(outset):
    return True


def backtracking_search(input, solSet):
    return recursive_backtracking(input, solSet)


def recursive_backtracking(assignment, solSet):
    if check_complete(assignment, solSet):
        return assignment
    var = select_unassigned_var(assignment)
    for var in range(1, 12):
        # Not sure about this. Somewhat sure it's ok (the program works haha)
        value = "A"
        if isValid(value, var, assignment):
            ass = list(assignment)
            ass[var] = value
            assignment = "".join(ass)
            result = recursive_backtracking(assignment, solSet)
            if result:
                return result
            else:
                ass = list(assignment)
                ass[var] = "0"
                assignment = "".join(ass)
    return None


def display(solution):
    result = ""
    for i in range(len(solution)):
        if i == 0: result += "  "
        if i == 5: result += "\n"
        if i == 12: result += "\n"
        if i == 19: result += "\n  "
        result += solution[i] + " "
    return result


def main():
    time1 = time.time()
    solSet = set()
    solution = 1
    while solution:
        solution = backtracking_search("T00000000000", solSet)

        solSet.add(solution)

    for arr in solSet:
        if arr:
            out = ""
            for index, val in enumerate(arr):
                if val != "0":
                    out += str(index) + " "
            print(out)

    print("\n" + str(len(solSet)))
    print("\nduration: " + str(time.time()-time1))


if __name__ == '__main__':
    main()
