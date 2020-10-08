import time
from concurrent.futures import ProcessPoolExecutor

from problem import Problem


def profile(f):
    print("started")
    start = time.perf_counter()
    output = f()
    end = time.perf_counter()

    return {"output": output, "time": end - start, "class": f.cls, "name": f.name}


def main():
    tasks = []
    with ProcessPoolExecutor(max_workers=10) as p:
        for problem in Problem.all_problems:
            for solution in problem.solutions:
                tasks.append(p.submit(profile, solution))
    print(tasks)


if __name__ == '__main__':
    main()
