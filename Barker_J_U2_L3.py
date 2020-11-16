# Name: Jeb Barker
# Date: 11-13-2020

def check_complete(assignment, csp_table):
    return True


def select_unassigned_var(assignment, variables, csp_table):
    return 0


def isValid(value, var_index, assignment, variables, csp_table):
    return True


def ordered_domain(assignment, variables, csp_table):
    return []


def update_variables(value, var_index, assignment, variables, csp_table):
    return {}


def backtracking_search(puzzle, variables, csp_table):
    return recursive_backtracking(puzzle, variables, csp_table)


def recursive_backtracking(assignment, variables, csp_table):
    return None


def display(solution):
    return ""


def sudoku_csp():
    # return [[x for x in range(1,82) if x % 9 == 1 or 2 or 3]]
    # return [[1,2,3,10,11,12,19,20,21]]
    out = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    for row in range(0, 9):
        for col in range(0, 9):
            out[9+row].append(row * 9 + col)
            out[18 + col].append(row * 9 + col)
            if col % 3 == 0:
                out[row // 3 + col // 3].append(*[row * 9 + col + x for x in range(0, 3)])

    return out


def initial_variables(puzzle, csp_table):
    out = {}
    for x in range(0,81):
        out[x] = [x for x in range(1,10)] if puzzle[x] == "." else [int(puzzle[x])]
    return out


def main():
    puzzle = input("Type a 81-char string:")
    while len(puzzle) != 81:
        print("Invalid puzzle")
        puzzle = input("Type a 81-char string: ")
    csp_table = sudoku_csp()
    variables = initial_variables(puzzle, csp_table)
    print("Initial:\n" + display(puzzle))
    solution = backtracking_search(puzzle, variables, csp_table)
    if solution != None:
        print("solution\n" + display(solution))
    else:
        print("No solution found.\n")


if __name__ == '_main_': main()