# Name: Jeb Barker
# Date: 11-13-2020
import copy
import time


def check_complete(assignment, csp_table):
    if assignment.find('.') != -1: return False
    for adj in csp_table:
        if len(set([assignment[i] for i in adj])) != 9: return False  # TODO? add case for '.'
    return True


def select_unassigned_var(assignment, variables, csp_table):
    smol = None
    for index, var in enumerate(assignment):
        if var == '.':
            if not smol:
                smol = index
            elif len(variables[index]) < len(variables[smol]):
                smol = index
    return smol


def isValid(value, var_index, assignment, variables, csp_table):
    for adj in csp_table:
        if var_index in adj:
            hTemp = set()
            for index in adj:
                hTemp.add(assignment[index])
            if value in hTemp:
                return False
    return True


def ordered_domain(assignment, variables, csp_table):
    return []


def update_variables(value, var_index, assignment, variables, csp_table):
    # out = {}
    for adj in csp_table:
        if var_index in adj:
            for var in adj:
                if value in variables[var] and var != var_index:
                    variables[var] = {a for a in variables[var] if a != value}
    return variables


def backtracking_search(puzzle, variables, csp_table):
    return recursive_backtracking(puzzle, variables, csp_table)


def recursive_backtracking(assignment, variables, csp_table):
    if check_complete(assignment, csp_table):
        return assignment
    var = select_unassigned_var(assignment, variables, csp_table)
    if var is None:
        return None
    for value in variables[var]:
        # if isValid(value, var, assignment, variables, csp_table):
        ass = list(assignment)
        ass[var] = str(value)
        assignment = "".join(ass)
        variablesbutcooler = {a: b for a, b in variables.items()} # variables.deepcopy()
        variablesbutcooler = update_variables(value, var, assignment, variablesbutcooler, csp_table)
        result = recursive_backtracking(assignment, variablesbutcooler, csp_table)
        if result:
            return result
        else:
            ass = list(assignment)
            ass[var] = "."
            assignment = "".join(ass)
    return None


def display(solution):
    result = ""
    for i in range(len(solution)):
        if i % 27 == 0 and i % 9 == 0 and i != 0: result += "\n"
        if i % 3 == 0 and i % 9 != 0: result += "  "  # Tab instead?
        if i % 9 == 0 and i !=0: result += "\n"
        if i == 0: result += "----------------------\n"
        result += solution[i] + " "
        if i == 80: result += "\n----------------------"
    return result


def sudoku_csp():
    # return [[x for x in range(1,82) if x % 9 == 1 or 2 or 3]]
    # return [[1,2,3,10,11,12,19,20,21]]
    out = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    for row in range(0, 9):
        for col in range(0, 9):
            out[9 + row].append(row * 9 + col)
            out[18 + col].append(row * 9 + col)
            if col % 3 == 0:
                for x in range(0, 3):
                    out[((row * 9 + col) // 9) - row % 3 + col // 3].append(row * 9 + col + x)

    return out


def initial_variables(puzzle, csp_table):
    out = {}
    for x in range(0, 81):
        out[x] = {y for y in range(1, 10)} if puzzle[x] == "." else {int(puzzle[x])}
    for var in out:
        for val in out[var]:
            if len(out[var]) == 1:
                update_variables(val, var, puzzle, out, csp_table)
    return out


def main():
    puzzle = input("Type a 81-char string:")
    if puzzle == "test":
        timeSet = []
        longPuzzles = []
        cur_time = time.time()
        csp_table = sudoku_csp()

        with open("longpuzzles") as f:
            for puzzle in f.readlines():
                cur_time = time.time()
                variables = initial_variables(puzzle, csp_table)
                solution = backtracking_search(puzzle, variables, csp_table)
                d = time.time() - cur_time
                timeSet.append(d)
                if d > 5:
                    longPuzzles.append(puzzle)
                print("solution\n" + display(solution))
                print(puzzle)
                print("duration: ", d)

        print("\nLong Puzzles (greater than 5 seconds)\n", *["\n" + a for a in longPuzzles])
        print("total time: ", sum(timeSet))
        print("average time: ", sum(timeSet) / len(timeSet))

    else:
        while len(puzzle) != 81:
            print("Invalid puzzle")
            puzzle = input("Type a 81-char string: ")
        cur_time = time.time()
        csp_table = sudoku_csp()
        print("csp time: ", (time.time() - cur_time))
        variables = initial_variables(puzzle, csp_table)
        print("Initial:\n" + display(puzzle))
        solution = backtracking_search(puzzle, variables, csp_table)
        if solution is not None:
            print("solution\n" + display(solution), "\n\nDuration: ", (time.time() - cur_time))
        else:
            print("No solution found.\n")


if __name__ == '__main__':
    main()

# ..7369825632158947958724316825437169791586432346912758289643571573291684164875293
# .3..5..4...8.1.5..46..12.7.5.2.8..6.3...4.1.9.3.25..98..1.2.6....8..6..2..8....27   54.95. .81 98.64. .2.4.3.6 69.51. .17 62.46 38 .9....


# '683942615495382672125567944936258427548711369741693858319475286854129733272836591'
