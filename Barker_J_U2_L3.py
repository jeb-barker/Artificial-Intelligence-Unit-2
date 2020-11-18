# Name: Jeb Barker
# Date: 11-13-2020
import copy


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
    if var == None:
        return None
    for value in sorted([a for a in variables[var]]):
        # if isValid(value, var, assignment, variables, csp_table):
        ass = list(assignment)
        ass[var] = str(value)
        assignment = "".join(ass)
        variablesbutcooler = copy.deepcopy(variables)
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


if __name__ == '__main__':
    main()

# ..7369825632158947958724316825437169791586432346912758289643571573291684164875293
# .3..5..4...8.1.5..46..12.7.5.2.8..6.3...4.1.9.3.25..98..1.2.6....8..6..2..8....27   54.95. .81 98.64. .2.4.3.6 69.51. .17 62.46 38 .9....

# .......1.4.........2...........5.4.7..8...3....1.9....3..4..2...5.1........8.6...
# 000000010400000000020000000000050604008000300001090000300400200050100000000807000
# 000000012000035000000600070700000300000400800100000000000120000080000040050000600
# 000000012003600000000007000410020000000500300700000600280000040000300500000000000
# 000000012008030000000000040120500000000004700060000000507000300000620000000100000
# .......12.4..5.........9....7.6..4.....1............5.....875..6.1...3..2........
# '683942615495382672125567944936258427548711369741693858319475286854129733272836591'
"""
003020600
900305001
001806400
008102900
700000008
006708200
002609500
800203009
005010300
========
200080300
060070084
030500209
000105408
000000000
402706000
301007040
720040060
004010003
========
000000907
000420180
000705026
100904000
050000040
000507009
920108000
034059000
507000000
========
030050040
008010500
460000012
070502080
000603000
040109030
250000098
001020600
080060020
========
020810740
700003100
090002805
009040087
400208003
160030200
302700060
005600008
076051090
========
100920000
524010000
000000070
050008102
000000000
402700090
060000000
000030945
000071006
========
043080250
600000000
000001094
900004070
000608000
010200003
820500000
000000005
034090710
========
480006902
002008001
900370060
840010200
003704100
001060049
020085007
700900600
609200018
========
000900002
050123400
030000160
908000000
070000090
000000205
091000050
007439020
400007000
========
001900003
900700160
030005007
050000009
004302600
200000070
600100030
042007006
500006800
========
000125400
008400000
420800000
030000095
060902010
510000060
000003049
000007200
001298000
========
062340750
100005600
570000040
000094800
400000006
005830000
030000091
006400007
059083260
========
300000000
005009000
200504000
020000700
160000058
704310600
000890100
000067080
000005437
========
630000000
000500008
005674000
000020000
003401020
000000345
000007004
080300902
947100080
========
000020040
008035000
000070602
031046970
200000000
000501203
049000730
000000010
800004000
========
361025900
080960010
400000057
008000471
000603000
259000800
740000005
020018060
005470329
========
050807020
600010090
702540006
070020301
504000908
103080070
900076205
060090003
080103040
========
.8...5........3457....7.8.9.6.4..9.3..7.1.5..4.8..7.2.9.1.2....8423........1...8.
"""
