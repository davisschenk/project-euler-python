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
            result = solution.profile()
            print(f"\t{solution.name}\n\t\tTime: {result.time.microseconds} ms\n\t\tOutput: {result.output}")
            if isinstance(result.output, Exception):
                traceback.print_tb(result.output.__traceback__)


def write_file():
    with open("output.csv", 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Problem", "Solution", "Execution Time (ms)", "Output"])

        for problem in Problem.all_problems():
            for solution in problem.solutions:
                result = solution.profile()

                writer.writerow([problem.name, solution.name, result.time.microseconds, result.output])


print_output()
