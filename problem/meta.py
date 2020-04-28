import problem
import time


class ProblemMeta(type):
    def __new__(mcs, *args, **kwargs):
        name, bases, attrs = args
        new_cls = type.__new__(mcs, name, bases, attrs)

        if new_cls.__name__ == "Problem":
            return new_cls

        new_cls.solutions = [obj for name, obj in attrs.items() if isinstance(obj, problem.Solution)]
        new_cls.name = kwargs.get("name") or new_cls.__name__
        new_cls._settings = kwargs

        # Add the problem to a list in Problem to keep track of all problems
        problem.Problem.all_problems.append(new_cls)

        return new_cls

    def __init__(cls, *args, **kwargs):
        name, bases, attrs = args
        # This is us telling each Solution which class it belongs to
        for solution in getattr(cls, "solutions", []):
            solution.cls = cls

        # Just a way to automatically call the function if the file is ran as main
        if cls.__module__ == '__main__':
            for solution in cls.solutions:
                start = time.perf_counter()
                output = solution()
                end = time.perf_counter()

                print(f"\t{solution.name}")
                print(f"\t\toutput: {output}")
                print(f"\t\ttotal time: {end - start:.8f}")

        type.__init__(cls, name, bases, attrs)
