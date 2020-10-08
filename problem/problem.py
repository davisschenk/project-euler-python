import problem


class Problem(metaclass=problem.ProblemMeta):
    all_problems = []

    @classmethod
    def solution(cls, **kwargs):
        def decorator(func):
            return problem.Solution(func, **kwargs)

        return decorator
