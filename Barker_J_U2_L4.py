# Name:
# Date:
import os, time

def initial_variables(puzzle, csp_table):
    out = {}
    for x in range(0, 81):
        out[x] = {y for y in range(1, 10)} if puzzle[x] == "." else {int(puzzle[x])}
    for var in out:
        for val in out[var]:
            if len(out[var]) == 1:
                update_variables(val, var, puzzle, out, csp_table)
    return out

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

def solve(puzzle, variables, csp_table):
    ''' suggestion:
    # q_table is quantity table {'1': number of value '1' occurred, ...}
    variables, puzzle, q_table = initialize_ds(puzzle, neighbors)
    return recursive_backtracking(puzzle, variables, neighbors, q_table)
    '''
    return recursive_backtracking(puzzle, variables, csp_table)


def sudoku_neighbors(csp_table):
    # each position p has its neighbors {p:[positions in same row/col/subblock], ...}
    return csp_table


def sudoku_csp(n=9):
    csp_table = [[k for k in range(i * n, (i + 1) * n)] for i in range(n)]  # rows
    csp_table += [[k for k in range(i, n * n, n)] for i in range(n)]  # cols
    temp = [0, 1, 2, 9, 10, 11, 18, 19, 20]
    csp_table += [[i + k for k in temp] for i in [0, 3, 6, 27, 30, 33, 54, 57, 60]]  # sub_blocks
    return csp_table


def checksum(solution):
    return sum([ord(c) for c in solution]) - 48 * 81  # One easy way to check a valid solution


def main():
    filename = input("file name: ")
    if not os.path.isfile(filename):
        filename = "puzzles.txt"
    csp_table = sudoku_csp()  # rows, cols, and sub_blocks

    neighbors = sudoku_neighbors(
        csp_table)  # each position p has its neighbors {p:[positions in same row/col/subblock], ...}
    start_time = time.time()
    for line, puzzle in enumerate(open(filename).readlines()):
        if line == 50: break  # check point: goal is less than 0.5 sec
        line, puzzle = line + 1, puzzle.rstrip()
        print("Line {}: {}".format(line, puzzle))
        variables = initial_variables(puzzle, csp_table)
        solution = solve(puzzle, variables, csp_table)
        if solution == None: print("No solution found."); break
        print("{}({}, {})".format(" " * (len(str(line)) + 1), checksum(solution), solution))
    print("Duration:", (time.time() - start_time))


if __name__ == '__main__': main()