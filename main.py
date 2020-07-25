import time

from problem import Problem

# TODO: Implement better profiling
for problem in Problem.all_problems:
    print(problem.name)

    for solution in problem.solutions:
        start = time.perf_counter()
        output = solution()
        end = time.perf_counter()

        print(f"\t{solution.name}")
        print(f"\t\toutput: {output}")
        print(f"\t\ttotal time: {end - start:.8f}")
