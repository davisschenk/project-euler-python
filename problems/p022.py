from utils import path
from problem import Problem


class NameScores(Problem, name="Names Scores", expected=871198282):
    """
    NOTE: I did some regex replace to convert the names file so each name is on its own line
    """
    @classmethod
    def load_names(cls):
        with path.load_file("p022_names.txt") as r:
            contents = r.read()
            names = [x.strip('"') for x in contents.split(",")]

        return sorted(names)

    @classmethod
    def calculate_name_score(cls, name):
        return sum(ord(n) - 64 for n in name)

    @Problem.solution()
    def solution(self):
        names = self.load_names()

        return sum((i+1) * self.calculate_name_score(name) for i, name in enumerate(names))
