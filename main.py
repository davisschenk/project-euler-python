from problem import Problem
import csv
import traceback

# We have to import all problems so that they get initialized and can be found
from problems import *


def print_output():
    for problem in Problem.all_problems():
        print(f"{problem.problem_number}. {problem.name}")
        print(f"\tExpected Value: {problem.expected}")
        for solution in problem.solutions:
            print(f"\t{solution.text()}")


def write_file():
    with open("output.csv", 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Problem", "Solution", "Execution Time (seconds)", "Output"])

        for problem in Problem.all_problems():
            print(problem.name)
            for solution in problem.solutions:
                result = solution.profile()

                writer.writerow([problem.name, solution.name, result.time, result.output])


write_file()
