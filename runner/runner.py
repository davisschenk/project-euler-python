import time
from concurrent.futures import ProcessPoolExecutor
from contextlib import redirect_stdout
from io import StringIO
from problems import *
from problem import Problem


class Runner:
    @staticmethod
    def profile_problem(problem: Problem):
        out = {"problem": problem.name, "solutions": []}
        for solution in problem.solutions:
            stdout = StringIO()
            try:
                with redirect_stdout(stdout):
                    start = time.perf_counter()
                    output = solution()
                    end = time.perf_counter()
            except Exception as exc:
                out["solutions"].append({"solution": solution.name, "error": exc})

            out["solutions"].append({
                "solution": solution.name,
                "time_seconds": end - start,
                "output": output,
                "stdout": stdout.read()
            })

        return out

    @classmethod
    def profile_problems(cls):
        with ProcessPoolExecutor(max_workers=10) as p:
            for output in p.map(cls.profile_problem, Problem.all_problems):
                print(output)


if __name__ == '__main__':
    Runner.profile_problems()
