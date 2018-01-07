# In this assignment you will implement one or more algorithms for the 2SAT problem. Here are 6 different 2SAT
# instances:

# 2sat1.txt
# 2sat2.txt
# 2sat3.txt
# 2sat4.txt
# 2sat5.txt
# 2sat6.txt

# The file format is as follows. In each instance, the number of variables and the number of clauses is the same, and
# this number is specified on the first line of the file. Each subsequent line specifies a clause via its two literals,
# with a number denoting the variable and a "-" sign denoting logical "not". For example, the second line of the first
# data file is "-16808 75250", which indicates the clause ¬x16808∨x75250.

# Your task is to determine which of the 6 instances are satisfiable, and which are unsatisfiable. In the box below,
# enter a 6-bit string, where the ith bit should be 1 if the ith instance is satisfiable, and 0 otherwise. For example,
# if you think that the first 3 instances are satisfiable and the last 3 are not, then you should enter the string
# 111000 in the box below.

# DISCUSSION: This assignment is deliberately open-ended, and you can implement whichever 2SAT algorithm you want.
# For example, 2SAT reduces to computing the strongly connected components of a suitable graph (with two vertices per
# variable and two directed edges per clause, you should think through the details). This might be an especially
# attractive option for those of you who coded up an SCC algorithm in Part 2 of this specialization. Alternatively, you
# can use Papadimitriou's randomized local search algorithm. (The algorithm from lecture is probably too slow as stated,
# so you might want to make one or more simple modifications to it --- even if this means breaking the analysis given in
# lecture --- to ensure that it runs in a reasonable amount of time.) A third approach is via backtracking. In lecture
# we mentioned this approach only in passing; see Chapter 9 of the Dasgupta-Papadimitriou-Vazirani book, for example,
# for more details.


import random
import math

"""
GenerateRandomAssignment(number_of_variables)
nbvar is the number of variables that are in the cnf, which the assignment is being created for
returns an array of length nbvar that has the value -1(false) or 1(true)
"""
def GenerateRandomAssignment(number_of_variables):
    random_assignment = []
    for i in range(number_of_variables):
        random_assignment.append(random.randrange(-1,2,2))
    return random_assignment



def Read2SAT(filename):
    problem_statement = []
    with open(filename, 'r') as SAT:
        variable_count = int(SAT.readline())
        for line in SAT:
            line = line.split()
            problem_statement.append([int(line[0]), int(line[1])])

    return variable_count, problem_statement

def VerifySolution(solution, problem_statement):
    errant_clauses = []
    for i, clause in enumerate(problem_statement):
        clause_valid = False
        for var in clause:
            clause_valid = clause_valid or \
                           solution[abs(var)-1] > 0 and var > 0 or \
                           solution[abs(var)-1] < 0 and var < 0
        if not clause_valid:
            errant_clauses.append(i)

    return errant_clauses

def RandomCorrection(assignment, problem_statement, errant_clauses):
    random_selection = random.randrange(0, len(errant_clauses))
    random_clause = errant_clauses[random_selection]
    random_var = random.randint(0,1)
    random_var_value = problem_statement[random_clause][random_var]

    assignment[abs(random_var_value)-1] = -1*assignment[abs(random_var_value)-1]

def Papadimitriou2Sat(var_count, problem_statement):

    restarts = int(math.log2(var_count))
    local_search_iterations = int(2 * math.pow(var_count, 2))

    for reset_count in range(restarts):
        print('Restart: {}'.format(reset_count))
        random_assignment = GenerateRandomAssignment(var_count)

        for _ in range(local_search_iterations):
            errant_clauses = VerifySolution(random_assignment, problem_statement)
            if not errant_clauses:
                return True, random_assignment
            else:
                RandomCorrection(random_assignment, problem_statement, errant_clauses)

    return False, random_assignment




if __name__ == '__main__':

    print('sat1')
    var_count, sat1 = Read2SAT('2sat1.txt')
    solved1, solution1 = Papadimitriou2Sat(var_count, sat1)
    print('sat1: {}'.format(solved1))

    var_count, sat2 = Read2SAT('2sat2.txt')
    solved2, solution2 = Papadimitriou2Sat(var_count, sat2)
    print('sat2: {}'.format(solved2))

    print('sat3')
    var_count, sat3 = Read2SAT('2sat3.txt')
    solved3, solution3 = Papadimitriou2Sat(var_count, sat3)
    print('sat3: {}'.format(solved3))

    print('sat4')
    var_count, sat4 = Read2SAT('2sat4.txt')
    solved4, solution4 = Papadimitriou2Sat(var_count, sat4)
    print('sat4: {}'.format(solved4))

    print('sat5')
    var_count, sat5 = Read2SAT('2sat5.txt')
    solved5, solution5 = Papadimitriou2Sat(var_count, sat5)
    print('sat5: {}'.format(solved5))

    print('sat6')
    var_count, sat6 = Read2SAT('2sat6.txt')
    solved6, solution6 = Papadimitriou2Sat(var_count, sat6)
    print('sat6: {}'.format(solved6))



    print('sat1: True')
    print('sat2: {}'.format(solved2))
    print('sat3: {}'.format(solved3))
    print('sat4: {}'.format(solved4))
    print('sat5: {}'.format(solved5))
    print('sat6: {}'.format(solved6))

