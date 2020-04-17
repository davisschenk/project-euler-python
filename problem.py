import time
from datetime import timedelta
import re


class SolutionOutput:
    def __init__(self, *, output, time):
        self.output = output
        self.time = time

    def __repr__(self):
        return f"(Solution output={self.output} time={self.time.microseconds} ms)"


class Solution:
    """A class that represents a problem solution"""

    def __init__(self, solution, name=None):
        self.solution = solution
        self.name = name or solution.__name__
        self.problem = None

    def __call__(self, *args, **kwargs):
        try:
            return self.solution(self=self.problem, *args, **kwargs)
        except Exception as exc:
            return exc

    def profile(self):
        start_time = time.perf_counter_ns()
        output = self.__call__()
        end_time = time.perf_counter_ns()

        return SolutionOutput(
            output=output,
            time=timedelta(microseconds=(end_time - start_time) / 1000)
        )


problems = []


class ProblemMeta(type):
    def __new__(mcs, *args, **kwargs):
        name, bases, attrs = args
        new_cls = super().__new__(mcs, name, bases, attrs)

        # TODO: Change this from using len of bases
        # Makes sure that we are modifying a subclass of Problem and not Problem and that Problem isnt being run as main
        if len(bases) > 0 and new_cls.__module__ != "__main__":
            new_cls.solutions = [obj for name, obj in attrs.items() if isinstance(obj, Solution)]
            new_cls.name = kwargs.pop("name")
            new_cls.expected = kwargs.pop("expected", None)
            new_cls.problem_number = re.search(r"\.([0-9]+)_", new_cls.__module__).group(1)

        return new_cls

    def __init__(cls, *args, **kwargs):
        name, bases, attrs = args

        # Adds the problem attr to each solution so we can use it as self
        if isinstance(getattr(cls, "solutions"), list):
            for name, obj in attrs.items():
                if isinstance(obj, Solution):
                    obj.problem = cls

            problems.append(cls)
        type.__init__(cls, name, bases, attrs)


class Problem(metaclass=ProblemMeta):
    __slots__ = ("cls", "solutions")

    def __init__(self, cls):
        self.cls = cls
        problems.append(cls)

    @classmethod
    def all_problems(cls):
        return problems

    @classmethod
    def solution(cls, name=None):
        """
        A Decorator to specify a Problem Solution
        :param name:
        :return:
        """

        def decorator(func):
            return Solution(func, name=name)

        return decorator
