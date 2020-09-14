from problem import Problem
from utils import path


def load_names():
    with path.load_file("p022_names.txt") as r:
        contents = r.read()
        names = [x.strip('"') for x in contents.split(",")]

    return sorted(names)


class NameScores(Problem, name="Names Scores", expected=871198282):
    names = load_names()

    @classmethod
    def calculate_name_score(cls, name):
        return sum(ord(n) - 64 for n in name)

    @Problem.solution()
    def solution(self):
        return sum((i + 1) * self.calculate_name_score(name) for i, name in enumerate(self.names))
